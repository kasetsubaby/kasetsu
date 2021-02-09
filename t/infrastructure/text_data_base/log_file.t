use Kasetsu::Base;
use Test2::V0;

use File::Temp;
use aliased 'Kasetsu::Infrastructure::TextDatabase::LogFile';
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
}

my %logfile_params = (
  max_lines => 10,
  record    => Record->new(
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
  my $tmp = File::Temp->new;
  my $file = LogFile->new(
    path => $tmp->filename,
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
  my $tmp = File::Temp->new;
  my $file = LogFile->new(
    path => $tmp->filename,
    %logfile_params,
  );

  my @rows = map { Row->new(a => $_, b => $_ * 2) } 1 .. 5;
  $file->append_rows(\@rows);

  my $fetch_rows = $file->fetch_all_rows();
  is [ reverse @rows ], $fetch_rows, '最後に追加した行から順番に取り出す';
};

subtest 'max_lines を超える行を保存しようとした場合' => sub {
  my $tmp = File::Temp->new;
  my $file = LogFile->new(
    path => $tmp->filename,
    %logfile_params,
    max_lines => 3,
  );

  my @rows = map { Row->new(a => $_, b => $_ * 2) } 1 .. 5;
  $file->append_rows(\@rows);

  is $file->fetch_all_rows()->@*, $file->max_lines;
};

subtest 'max_lines と同じ行を保存しようとした場合' => sub {
  my $tmp = File::Temp->new;
  my $file = LogFile->new(
    path => $tmp->filename,
    %logfile_params,
    max_lines => 3,
  );

  my @rows = map { Row->new(a => $_, b => $_ * 2) } 1 .. 3;
  $file->append_rows(\@rows);

  is $file->fetch_all_rows()->@*, $file->max_lines;
};

subtest 'max_lines より少ない行を保存しようとした場合' => sub {
  my $tmp = File::Temp->new;
  my $file = LogFile->new(
    path => $tmp->filename,
    %logfile_params,
    max_lines => 3,
  );

  my $append_rows_num = 2;
  my @rows = map { Row->new(a => $_, b => $_ * 2) } 1 .. $append_rows_num;
  $file->append_rows(\@rows);

  is $file->fetch_all_rows()->@*, $append_rows_num;
};

done_testing;
