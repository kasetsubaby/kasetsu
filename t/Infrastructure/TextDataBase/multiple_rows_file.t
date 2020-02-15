use Kasetsu::Base;
use Test2::V0;

use File::Temp;
use aliased 'Kasetsu::Infrastructure::TextDatabase::MultipleRowsFile';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';

package Row {
  use Kasetsu::Base;
  use Mouse;

  has index => (
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has a => (
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has b => (
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  __PACKAGE__->meta->make_immutable;
}

my $fh = File::Temp->new;
my $file = MultipleRowsFile->new(
  path      => $fh->filename,
  dto_class => 'Row',
  columns   => Columns->new(
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
  ),
);

subtest 'store_all_rows and fetch_all_rows' => sub {
  my @rows = map {
    Row->new(
      index => $_,
      a     => 1,
      b     => 2,
    );
  } 0 .. 4;
  $file->store_all_rows(\@rows);
  my $fetch_rows = $file->fetch_all_rows();
  is \@rows, $fetch_rows;
};

subtest 'store_row_of and fetch_row_of' => sub {
  my $row = Row->new(
    index => 3,
    a     => 1,
    b     => 2,
  );
  $file->store_row($row);
  my $fetch_row = $file->fetch_row_of($row->index);
  is $row, $fetch_row;
};

done_testing;
