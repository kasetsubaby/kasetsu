package Kasetsu::Exception;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use overload (
  q{""}     => sub { shift->to_string },
  fallback => 1,
);

# abstract
sub message {
  die 'Can not call abstract method.';
}

has frames => (
  is       => 'ro',
  required => 1,
);

sub throw {
  my $class = shift;
  die $class->new(frames => $class->trace(1), @_);
}

sub trace {
  state $c = compile(Invocant, Str);
  my ($class, $start) = $c->(@_);

  my @frames;
  while ( my @frame = caller($start++) ) {
    push @frames, \@frame;
  }
  \@frames;
}

sub to_string {
  my $self = shift;

  my $str = $self->message;
  my $frames = $self->frames;

  # 例外クラスから例外投げたときはメッセージのあとに例外を投げた場所を追記する
  if ($str !~ /\n$/) {
    $str .= @$frames ? " at $frames->[0][1] line $frames->[0][2].\n" : "\n";
  }

  for my $frame (@$frames) {
    $str .= qq{\t$frame->[3] called at $frame->[1] line $frame->[2]\n};
  }

  $str;
}

__PACKAGE__->meta->make_immutable;

1;
