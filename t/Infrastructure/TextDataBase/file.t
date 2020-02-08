use Kasetsu::Base;
use Test2::V0;

use File::Temp;
use aliased 'Kasetsu::Infrastructure::TextDatabase::File';

package Row {
  use Mouse;
  BEGIN { with 'Kasetsu::Infrastructure::TextDatabase::DTO' }
  __PACKAGE__->meta->make_immutable;
}

my $fh = File::Temp->new;
my $file = File->new(
  path      => $fh->filename,
  dto_class => 'Row',
);

ok $file->exists;
ok $file->remove;
ok !$file->exists;
ok $file->touch;
ok $file->exists;

done_testing;
