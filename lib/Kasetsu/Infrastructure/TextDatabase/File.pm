package Kasetsu::Infrastructure::TextDatabase::File;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { with 'Kasetsu::Infrastructure::TextDatabase::Collection' }

use aliased 'Kasetsu::Infrastructure::TextDatabase::Decoder';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Encoder';
use aliased 'Kasetsu::Infrastructure::TextDatabase::SaveDataWithCompatibleFileLock';

has decoder => (
  is      => 'ro',
  isa     => InstanceOf[Decoder],
  lazy    => 1,
  default => sub {
    my $self = shift;
    Decoder->new(record => $self->record);
  },
);

has encoder => (
  is      => 'ro',
  isa     => InstanceOf[Encoder],
  lazy    => 1,
  default => sub {
    my $self = shift;
    Encoder->new(record => $self->record);
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

sub is_exists {
  my $self = shift;
  -e $self->path;
}

sub remove {
  my $self = shift;
  unlink $self->path or die $!;
}

__PACKAGE__->meta->make_immutable;

1;
