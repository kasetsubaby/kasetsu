package Kasetsu::Infrastructure::TextDatabase::Declare;
use Kasetsu::Base;
use Exporter qw( import );

use aliased 'Kasetsu::Infrastructure::TextDatabase::Database';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Directory';
use aliased 'Kasetsu::Infrastructure::TextDatabase::SingleRowFile';
use aliased 'Kasetsu::Infrastructure::TextDatabase::MultipleRowsFile';
use aliased 'Kasetsu::Infrastructure::TextDatabase::LogFile';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Record' => 'Record', qw( RecordType );
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column' => 'Column', qw( AccessControlType TypeConstraintType );
use aliased 'Kasetsu::Infrastructure::TextDatabase::NestedColumn';
use aliased 'Kasetsu::Infrastructure::TextDatabase::JSONColumn';
use Kasetsu::Infrastructure::TextDatabase::MetaDTOClassCreator qw( create_meta_dto_class );
use Kasetsu::Infrastructure::TextDatabase::Exporter qw( MaybeClassName );
use Hash::Util qw( lock_ref_keys );
use Class::Load qw( is_class_loaded );
use Kasetsu::Home qw( detect_home_dir );

{
  my @class_methods = qw( database );

  my @dsls = qw(
    directory
    single_row_file
    multiple_rows_file
    log_file
    collection
    path
    file_class
    record
    dto_class
    column
    attribute
    nested_column
    json_column
  );

  my @file_classes_alias = qw(
    SingleRowFile
    MultipleRowsFile
    LogFile
  );

  our @EXPORT = (@class_methods, @dsls, @file_classes_alias);
}

sub database {
  state $c = compile(ClassName);
  my $class = $c->(@_);
  state %database_of;
  $database_of{$class} //= Database->new;
}

sub collection (&) { shift }

{
  my %Building_data;

  sub directory($$) {
    state $c = compile(Str, CodeRef);
    my ($name, $code) = $c->(@_);

    my $dir = do {
      local $Building_data{collection_params} = lock_ref_keys({
        path       => undef,
        file_class => undef,
        record     => undef,
      });
      $code->();
      Directory->new($Building_data{collection_params});
    };

    my $klass = caller;
    $klass->database->add_collection($name => $dir);

    %Building_data = ();
  }

  sub single_row_file($$) {
    state $c = compile(Str, CodeRef);
    my ($name, $code) = $c->(@_);

    my $file = do {
      local $Building_data{collection_params} = lock_ref_keys({
        path   => undef,
        record => undef,
      });
      $code->();
      SingleRowFile->new($Building_data{collection_params});
    };

    my $klass = caller;
    $klass->database->add_collection($name => $file);

    %Building_data = ();
  }
  
  sub multiple_rows_file {
    state $c = compile(Str, CodeRef);
    my ($name, $code) = $c->(@_);

    my $file = do {
      local $Building_data{collection_params} = lock_ref_keys({
        path   => undef,
        record => undef,
      });
      $code->();
      MultipleRowsFile->new($Building_data{collection_params});
    };

    my $klass = caller;
    $klass->database->add_collection($name => $file);

    %Building_data = ();
  }
  
  sub log_file {
    state $c = compile(Str, CodeRef);
    my ($name, $code) = $c->(@_);

    my $file = do {
      local $Building_data{collection_params} = lock_ref_keys({
        path   => undef,
        record => undef,
      });
      $code->();
      LogFile->new($Building_data{collection_params});
    };

    my $klass = caller;
    $klass->database->add_collection($name => $file);

    %Building_data = ();
  }

  sub path($) {
    state $c = compile(Str);
    my ($path) = $c->(@_);

    # script ディレクトリ以下で起動したcgiから使う場合と
    # プロジェクトルートから起動した場合の差異を埋めるため
    # 絶対パス指定にする
    my $abs_path = File::Spec->catfile(detect_home_dir(), 'script', $path);

    $Building_data{collection_params}{path} = $abs_path;
  }

  sub file_class($) {
    state $c = compile(Enum[ SingleRowFile, MultipleRowsFile, LogFile ]); 
    my ($file_class) = $c->(@_);
    $Building_data{collection_params}{file_class} = shift;
  }

  sub record(&) {
    my $code = shift;

    local $Building_data{record_params} = lock_ref_keys({
      dto_class        => undef,
      attributes       => [],
      columns_contents => [],
    });
    local $Building_data{record_dto_class_attributes} = [];
    $code->();

    my ($dto_class, $attributes, $columns_contents) =
      $Building_data{record_params}->@{qw( dto_class attributes columns_contents )};

    # dto_class が loaded ならそのまま渡す, loaded でないなら動的にクラスを作って型を作る
    unless ( is_class_loaded($dto_class) ) {
      my @attributes_params = (
        @$attributes,
        map {
          +{
            name => $_->name,
            is   => $_->access_control,
            isa  => $_->type_constraint,
          };
        } @$columns_contents
      );

      my $klass = create_meta_dto_class($dto_class, \@attributes_params);
      state %dto_klass_of;
      $dto_klass_of{ $klass->name } //= $klass;
    }

    my $record = Record->new(
      dto_class => $dto_class,
      columns   => Columns->new(contents => $columns_contents),
    );
    $Building_data{collection_params}{record} = $record;
  }

  sub attribute {
    my $name = shift;
    state $c = compile_named(
      is  => AccessControlType,
      isa => TypeConstraintType,
    );
    my $args = $c->(@_);

    push $Building_data{record_params}{attributes}->@*, +{ name => $name, %$args };
  }

  sub dto_class($) {
    state $c = compile(MaybeClassName);
    my ($dto_class) = $c->(@_);
    $Building_data{record_params}{dto_class} = $dto_class;
  }
  
  sub column {
    my $name = shift;
    state $c = compile_named(
      is  => AccessControlType,
      isa => TypeConstraintType,
    );
    my $args = $c->(@_);

    push $Building_data{record_params}{columns_contents}->@*, Column->new(
      name            => $name,
      access_control  => $args->{is},
      type_constraint => $args->{isa},
    );
  }

  sub nested_column {
    my $name = shift;
    state $c = compile_named(
      is        => AccessControlType,
      separator => Optional[Str],
      record    => RecordType,
    );
    my $args = $c->(@_);

    push $Building_data{record_params}{columns_contents}->@*, NestedColumn->new(
      name           => $name,
      access_control => $args->{is},
      record         => $args->{record},
      exists $args->{separator} ? ( separator => $args->{separator} ) : (),
    );
  }
  
  sub json_column {
    my $name = shift;
    state $c = compile_named(
      is     => AccessControlType,
      record => RecordType,
    );
    my $args = $c->(@_);

    push $Building_data{record_params}{columns_contents}->@*, JSONColumn->new(
      name           => $name,
      access_control => $args->{is},
      record         => $args->{record},
    );
  }
}

1;

__END__

