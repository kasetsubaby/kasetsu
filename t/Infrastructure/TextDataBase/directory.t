use Kasetsu::Base;
use Test2::V0;

use File::Temp;
use File::Spec;
use Mouse::Meta::Class;
use Mouse::Meta::Attribute;
use aliased 'Kasetsu::Infrastructure::TextDatabase::Directory';
use aliased 'Kasetsu::Infrastructure::TextDatabase::SingleFile';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Record';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';

sub create_class {
  my ($class_name, $columns) = @_;
  my @attributes = map {
    Mouse::Meta::Attribute->new(
      $_->name,
      is       => $_->access_control,
      isa      => $_->type_constraint,
      required => 1,
    );
  } @$columns;
  my $class = Mouse::Meta::Class->create(
    $class_name,
    superclasses => ['Mouse::Object'],
    attributes   => \@attributes,
  );
}

my $columns = Columns->new(
  contents => [
    Column->new(
      name            => 'a',
      access_control  => 'ro',
      type_constraint => Int,
    ),
    Column->new(
      name            => 'b',
      access_control  => 'ro',
      type_constraint => Int,
    ),
  ],
);
my $row_class = create_class('Row' => $columns);

my $tmpdir = File::Temp->newdir();
my $dir = Directory->new(
  path       => $tmpdir->dirname,
  file_class => SingleFile,
  record     => Record->new(
    dto_class => 'Row',
    columns   => $columns,
  ),
);

my $file = $dir->file_of_id('some_id');
is $file->path, File::Spec->catfile($dir->path, 'some_id.cgi');
my @files = map { $dir->file_of_id($_) } 'a' .. 'e';
$_->touch() for @files;
is $dir->all_exists_files, array {
  item object { prop blessed => SingleFile } for 1 .. 5;
  end;
};

ok 1;

done_testing;
