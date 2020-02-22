use Kasetsu::Base;
use Test2::V0;

use File::Temp;
use aliased 'Kasetsu::Infrastructure::TextDatabase::SingleFile';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Record';

package Row {
  use Kasetsu::Base;
  use Mouse;

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
my $file = SingleFile->new(
  path   => $fh->filename,
  record => Record->new(
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
  ),
);

subtest 'store and fetch row' => sub {
  my $row = Row->new(a => 1, b => 2);
  $file->store_row($row);
  my $fetched_row = $file->fetch_row();
  is $fetched_row, object {
    prop blessed => 'Row';
    call a => 1;
    call b => 2;
  };
};

done_testing;
