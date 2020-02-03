package Kasetsu::Infrastructure::TextDatabase::File;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use Types::Standard qw( Str InstanceOf );
use Kasetsu::Infrastructure::TextDatabase::DTO::Exporter qw( DTOClassType );
use aliased 'Kasetsu::Infrastructure::TextDatabase::Decoder';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Encoder';

has name => (
  is       => 'ro',
  isa      => Str,
  required => 1,
);

has dto_class => (
  is       => 'ro',
  isa      => DTOClassType,
  required => 1,
);

has decoder => (
  is      => 'ro',
  isa     => InstanceOf[Decoder],
  lazy    => 1,
  default => sub {
    my $self = shift;
    Decoder->new(dto_class => $self->dto_class);
  },
);

has encoder => (
  is      => 'ro',
  isa     => InstanceOf[Encoder],
  lazy    => 1,
  default => sub {
    my $self = shift;
    Encoder->new();
  },
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
