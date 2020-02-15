use Kasetsu::Base;
use Test2::V0;

use File::Temp;
use aliased 'Kasetsu::Infrastructure::TextDatabase::File';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';

package Row {
  use Mouse;
  has a => (
    is       => 'ro',
    required => 1,
  );
}

my $fh = File::Temp->new;
my $file = File->new(
  path      => $fh->filename,
  dto_class => 'Row',
  columns   => Columns->new(
    contents => [
      Column->new(
        name            => 'a',
        access_control  => 'ro',
        type_constraint => Str,
      ),
    ],
  ),
);

ok $file->exists;
ok $file->remove;
ok !$file->exists;
ok $file->touch;
ok $file->exists;

done_testing;
