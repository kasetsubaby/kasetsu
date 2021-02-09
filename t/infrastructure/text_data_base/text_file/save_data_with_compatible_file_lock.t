use Kasetsu::Base;
use Test2::V0;

use File::Temp;
use Test::MockTime qw( set_fixed_time );
use Path::Tiny qw( path );
use aliased 'Kasetsu::Infrastructure::TextDatabase::TextFile::SaveDataWithCompatibleFileLock';

my $file = SaveDataWithCompatibleFileLock->new(
  path          => File::Temp->new->filename,
  tmpfile_path  => path( File::Temp->new->filename ),
  lockfile_path => path( File::Temp->new->filename ),
);

subtest 'save data' => sub {
  ok !$file->is_locked();
  $file->save_data(['hoge']);
  ok !$file->is_locked();
  is $file->path->slurp(), 'hoge';
};

subtest 'is_locked' => sub {

  subtest 'lockfileが存在しているときはロック中' => sub {
    $file->lockfile_path->touch();
    ok $file->is_locked();
    $file->unlock();
  };

  subtest 'tmpfileが存在しているときはロック中' => sub {
    $file->tmpfile_path->touch();
    ok $file->is_locked();
    $file->unlock();
  };
  
  subtest '10秒経ったら前のファイル書き込み処理が完了したとみなしてロック解除される' => sub {
    $file->lockfile_path->touch(time - 11);
    ok !$file->is_locked();
  };

};

ok 1;

done_testing;
