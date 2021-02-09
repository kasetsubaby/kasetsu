use Kasetsu::Base;
use Test2::V0;

use File::Temp;
use aliased 'Kasetsu::Infrastructure::TextDatabase::HugeLogFile';
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

my %logfile_params = (
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

subtest 'append_row and fetch_rows' => sub {
  my $file = HugeLogFile->new(
    path => File::Temp->new->filename,
    %logfile_params,
  );

  my $row = Row->new(a => 5, b => 2);
  $file->append_row($row);

  my $row2 = Row->new(a => 0, b => 0);
  $file->append_row($row2);

  my $fetch_rows = $file->fetch_rows(2);
  is [ $row2, $row ], $fetch_rows;
};

subtest 'append_rows and fetch_all_rows' => sub {
  my $file = HugeLogFile->new(
    path => File::Temp->new->filename,
    %logfile_params,
  );

  my @rows = map { Row->new(a => $_, b => $_ * 2) } 1 .. 5;
  $file->append_rows(\@rows);

  my $fetch_rows = $file->fetch_all_rows();
  is [ reverse @rows ], $fetch_rows, '最後に追加した行から順番に取り出す';
};

done_testing;
