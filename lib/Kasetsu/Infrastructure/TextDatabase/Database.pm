package Kasetsu::Infrastructure::TextDatabase::Database;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use aliased 'Kasetsu::Infrastructure::TextDatabase::Collection';

has _collection_of_name => (
  is      => 'ro',
  isa     => Dict[ Str, ConsumerOf[Collection] ],
  default => sub { +{} },
);

sub add_collection {
  state $c = compile(Invocant, Str, ConsumerOf[Collection]);
  my ($self, $name, $collection) = $c->(@_);
  $self->_collection_of_name->{$name} = $collection;
}

__PACKAGE__->meta->make_immutable;

1;
