use Kasetsu::Base;
use Test2::V0;

use File::Temp;
use aliased 'Kasetsu::Infrastructure::TextDatabase::TextFile';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Record';

package Row {
  use Mouse;
  has a => (
    is       => 'ro',
    required => 1,
  );
}

my $fh = File::Temp->new;
my $file = TextFile->new(
  path   => $fh->filename,
  record => Record->new(
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
  ),
);

ok $file->is_exists;
ok $file->remove;
ok !$file->is_exists;
ok $file->touch;
ok $file->is_exists;

done_testing;
