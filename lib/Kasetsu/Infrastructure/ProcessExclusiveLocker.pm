package Kasetsu::Infrastructure::ProcessExclusiveLocker;
use Kasetsu::Base;
use Mouse;
use Exporter qw( import );

use File::stat qw( stat );
use Sub::Retry qw( retry );

our @EXPORT_OK = ('CannotLockException');

# alias
use constant CannotLockException =>
  'Kasetsu::Infrastructure::ProcessExclusiveLocker::CannotLockException';

use constant FORCE_UNLOCK_TIME => 30;
use constant RETRY_TIMES       => 3;
use constant RETRY_DELAY       => 0.1;

has dirname => (
  is       => 'ro',
  isa      => Str,
  required => 1,
);

sub lock {
  my $self = shift;

  # 前回のプロセス実行から長時間経過している場合は強制的にロック解除する
  if ( -d $self->dirname && time - stat($self->dirname)->mtime > FORCE_UNLOCK_TIME ) {
    $self->unlock();
  }

  retry RETRY_TIMES, RETRY_DELAY, sub {
    mkdir $self->dirname or CannotLockException->throw(errno => $!);
  };
}

sub unlock {
  my $self = shift;
  rmdir $self->dirname;
}

__PACKAGE__->meta->make_immutable;

package Kasetsu::Infrastructure::ProcessExclusiveLocker::CannotLockException;
use Kasetsu::Base;
use Mouse;
BEGIN { extends 'Kasetsu::Exception' }

# override
sub message {
  my $self = shift;
  qq{排他ロックを取得できませんでした。 errno: @{[ $self->errno ]}};
}

has errno => (
  is       => 'ro',
  isa      => Str,
  required => 1,
);

1;
