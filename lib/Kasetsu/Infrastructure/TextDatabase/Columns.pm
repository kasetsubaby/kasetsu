package Kasetsu::Infrastructure::TextDatabase::Columns;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';

use overload (
  '@{}'    => 'as_arrayref',
  fallback => 1,
);

use List::Util qw( uniq );

has contents => (
  is       => 'ro',
  isa      => ArrayRef[ InstanceOf[Column] ],
  required => 1,
);

sub BUILD {
  my $self = shift;
  my @contents = $self->contents->@*;
  unless ( @contents == uniq map { $_->name } @contents ) {
    die '重複しているカラム名があります。';
  }
}

sub as_arrayref { $_[0]->contents }

__PACKAGE__->meta->make_immutable;

1;
