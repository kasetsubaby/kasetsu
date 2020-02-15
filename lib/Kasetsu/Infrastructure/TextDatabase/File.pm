package Kasetsu::Infrastructure::TextDatabase::File;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Decoder';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Encoder';
use aliased 'Kasetsu::Infrastructure::TextDatabase::SaveDataWithCompatibleFileLock';

has path => (
  is       => 'ro',
  isa      => Str,
  required => 1,
);

has dto_class => (
  is       => 'ro',
  isa      => ClassName,
  required => 1,
);

has columns => (
  is       => 'ro',
  isa      => InstanceOf[Columns],
  required => 1,
);

has decoder => (
  is      => 'ro',
  isa     => InstanceOf[Decoder],
  lazy    => 1,
  default => sub {
    my $self = shift;
    Decoder->new(
      dto_class => $self->dto_class,
      columns   => $self->columns,
    );
  },
);

has encoder => (
  is      => 'ro',
  isa     => InstanceOf[Encoder],
  lazy    => 1,
  default => sub {
    my $self = shift;
    Encoder->new(
      dto_class => $self->dto_class,
      columns   => $self->columns,
    );
  },
);

has data_saver => (
  is      => 'ro',
  isa     => InstanceOf[SaveDataWithCompatibleFileLock],
  lazy    => 1,
  default => sub {
    my $self = shift;
    SaveDataWithCompatibleFileLock->new(path => $self->path);
  },
);

sub touch {
  my $self = shift;
  open my $fh, '>', $self->path or die $!;
  $fh->close();
}

sub exists {
  my $self = shift;
  -e $self->path;
}

sub remove {
  my $self = shift;
  unlink $self->path or die $!;
}

__PACKAGE__->meta->make_immutable;

1;
