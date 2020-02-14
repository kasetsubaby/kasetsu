package Kasetsu::Infrastructure::TextDatabase::Column;
use Kasetsu::Base;
use Mouse;
use Type::Tiny;
use namespace::autoclean;

use constant AccessControlType => Type::Tiny->new(
  name       => 'AccessControlType',
  parent     => Str,
  constraint => sub {
    my $got = shift;
    $got eq 'ro' || $got eq 'rw';
  },
);

has name => (
  is       => 'ro',
  isa      => Str,
  required => 1,
);

has access_control => (
  is       => 'ro',
  isa      => AccessControlType,
  required => 1,
);

has type_constraint => (
  is       => 'ro',
  isa      => HasMethods[qw( check get_message )],
  required => 1,
);

__PACKAGE__->meta->make_immutable;

1;
