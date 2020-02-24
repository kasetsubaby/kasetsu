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
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column' => 'Column',
  qw( AccessControlType TypeConstraintType );
use aliased 'Kasetsu::Infrastructure::TextDatabase::NestedColumn';
use aliased 'Kasetsu::Infrastructure::TextDatabase::JSONColumn';

my @class_methods = qw( database );

my @dsls = qw(
  directory
  single_row_file
  multiple_rows_file
  log_file
  record
  columns
  column
  nested_column
  json_column
);

our @EXPORT = (@class_methods, @dsls);

sub database {
  state $c = compile(ClassName);
  my $class = $c->(@_);
  state %database_of;
  $database_of{$class} //= Database->new;
}

sub directory {
  my $dir = Directory->new(@_);
  my $klass = caller;
  $klass->add_collection($dir);
}

sub single_row_file {
  my $file = SingleRowFile->new(@_);
  my $klass = caller;
  $klass->add_collection($file);
}

sub multiple_rows_file {
  my $file = MultipleRowsFile->new(@_);
  my $klass = caller;
  $klass->add_collection($file);
}

sub log_file {
  my $file = Directory->new(@_);
  my $klass = caller;
  $klass->add_collection($file);
}

sub record {
  Record->new(@_);
}

sub columns {
  my $c = compile(ArrayRef[Column]);
  my ($columns) = $c->(\@_);
  Columns->new(contents => @_);
}

sub column {
  my $name = shift;
  my $c = compile_named(
    is  => AccessControlType,
    isa => TypeConstraintType,
  );
  my $args = $c->(@_);
  Column->new(
    name            => $name,
    access_control  => $args->{is},
    type_constraint => $args->{isa},
  );
}

sub nested_column {
  my $name = shift;
  my $c = compile_named(
    is        => AccessControlType,
    record    => RecordType,
    separator => Optional[Str],
  );
  my $args = $c->(@_);
  NestedColumn->new(
    name           => $name,
    access_control => $args->{is},
    record         => $args->{record},
    exists $args->{separator} ? ( separator => $args->{separator} ) : (),
  );
}

sub json_column {
  my $name = shift;
  my $c = compile_named(
    is     => AccessControlType,
    record => RecordType,
  );
  my $args = $c->(@_);
  JSONColumn->new(
    name           => $name,
    access_control => $args->{is},
    record         => $args->{record},
  );
}

1;

__END__

directory name => (
  path       => '',
  file_class => '',
  record     => record(
    dto_class => '',
    columns   => columns(
      column name => (
        is => 'ro',
        isa => Str,
      ),
      column name2 => (
        is => 'ro',
        isa => Str,
      ),
    ),
  ),
);

single_row_file user => (
  path       => '',
  record     => record(
    dto_class => '',
    columns   => columns(
      column name => (
        is => 'ro',
        isa => Str,
      ),
      column name2 => (
        is => 'ro',
        isa => Str,
      ),
    ),
  ),
);
