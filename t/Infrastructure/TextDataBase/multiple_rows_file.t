use Kasetsu::Base;
use Test2::V0;

use File::Temp;
use aliased 'Kasetsu::Infrastructure::TextDatabase::SingleFile';

package Row {
  use Mouse;
  BEGIN { with 'Kasetsu::Infrastructure::TextDatabase::DTO' }

  use Kasetsu::Infrastructure::TextDatabase::DTO::Exporter;

  use Types::Standard qw( Int );

  has a => (
    metaclass => Column,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has b => (
    metaclass => Column,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  __PACKAGE__->meta->make_immutable;
}

my $fh = File::Temp->new;
my $file = SingleFile->new(
  path      => $fh->filename,
  dto_class => 'Row',
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
