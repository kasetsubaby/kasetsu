package Kasetsu::Infrastructure::TextDatabase::Database;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use aliased 'Kasetsu::Infrastructure::TextDatabase::Collection';

has _collection_of_name => (
  is      => 'ro',
  isa     => Map[ Str, ConsumerOf[Collection] ],
  default => sub { +{} },
);

sub get_collection {
  state $c = compile(Invocant, Str);
  my ($self, $name) = $c->(@_);
  $self->_collection_of_name->{$name} // die "Collection '$name' does not exists.";
}

sub get_dto_class_type {
  state $c = compile(Invocant, Str);
  my ($self, $name) = $c->(@_);
  my $collection = $self->get_collection($name);
  InstanceOf[ $collection->record->dto_class ];
}

sub add_collection {
  state $c = compile(Invocant, Str, ConsumerOf[Collection]);
  my ($self, $name, $collection) = $c->(@_);
  if ( exists $self->_collection_of_name->{$name} ) {
    die "Collection '$name' already exists.";
  }
  $self->_collection_of_name->{$name} = $collection;
}

__PACKAGE__->meta->make_immutable;

1;
