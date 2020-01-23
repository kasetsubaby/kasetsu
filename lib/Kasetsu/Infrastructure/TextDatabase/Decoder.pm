package Kasetsu::Infrastructure::TextDatabase::Decoder;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use aliased 'Kasetsu::Infrastructure::TextDatabase::DTO::MetaAttribute::Column';
use Types::Standard qw( Str ArrayRef InstanceOf );

has separator => (
  is      => 'ro',
  isa     => Str,
  default => '<>',
);

has columns => (
  is       => 'ro',
  isa      => ArrayRef[ InstanceOf[Column] ],
  required => 1,
);

has column_names => (
  is      => 'ro',
  # isa => ArrayRef[Str],
  lazy    => 1,
  builder => '_build_column_names',
);

sub _build_column_names {
  my $self = shift;
  my @meta_attrs = $self->dto_classs->
}

sub decode {
  my $line = shift;
}

__PACKAGE__->meta->make_immutable;

1;
