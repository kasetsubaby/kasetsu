package Kasetsu::Infrastructure::TextDatabase::File;
use Kasetsu::Base;
use Mouse;
use Type::Tiny;
use Type::Params qw( validate );
use Types::Standard qw( Str ClassName );
use Function::Return;
use namespace::autoclean;

has name => (
  is       => 'ro',
  isa      => Str,
  required => 1,
);

has dto_class => (
  is       => 'ro',
  isa      => ClassName->where(sub { $_->isa('Kasetsu::Infrastructure::TextDatabase::DTO') }),
  required => 1,
);

sub touch {
  my $self = shift;
  open my $fh, '>', $self->name or die $!;
  $fh->close();
}

sub exists {
  my $self = shift;
  -e $self->name;
}

sub remove {
  my $self = shift;
  unlink $self->name or die $!;
}

__PACKAGE__->meta->make_immutable;

1;
