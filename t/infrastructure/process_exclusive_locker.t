use Kasetsu::Base;
use Test2::V0;
use aliased (
  'Kasetsu::Infrastructure::ProcessExclusiveLocker' => 'ProcessExclusiveLocker',
  ('CannotLockException')
);

my $locker = ProcessExclusiveLocker->new(dirname => '/tmp/kasetsu_test');

ok $locker->lock();
my $e = dies { $locker->lock() };
ok $e->isa(CannotLockException);
ok $locker->unlock();

done_testing;
