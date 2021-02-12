use v5.32;
use strictures version => 2;
use utf8;
use Test2::V0;

use Kasetsu::Type::Utils::Generics::AlternativeTypes -types;

package User {
  use Mouse;
  has name => ( is => 'ro' );
}

package Player {
  use Mouse;
  has name => ( is => 'ro' );
}

my $airi = User->new(name => '桃井愛莉');

subtest 'InstanceOf' => sub {
  is InstanceOf(['User']), 'InstanceOf[User]';
  ok InstanceOf(['User'])->check($airi);
  ok !InstanceOf(['Player'])->check($airi);
  ok InstanceOf->check($airi);
  ok InstanceOf([])->check($airi);
};

package Singer {
  use Mouse::Role;
  sub sing { ... }
}

package Dancer {
  use Mouse::Role;
  sub dance { ... }
}

package Idle {
  use Mouse;
  with qw( Singer Dancer );
}

my $minori = Idle->new;

subtest 'ConsumerOf' => sub {
  is ConsumerOf(['Singer']), 'ConsumerOf[Singer]';
  ok ConsumerOf(['Singer'])->check($minori);
  ok ConsumerOf(['Dancer'])->check($minori);
  ok !ConsumerOf(['Singer'])->check($airi);
  ok ConsumerOf->check($minori);
  ok ConsumerOf([])->check($minori);
};

done_testing;
