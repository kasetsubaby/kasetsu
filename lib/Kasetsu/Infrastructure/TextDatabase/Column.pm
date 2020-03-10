package Kasetsu::Infrastructure::TextDatabase::Column;
use Kasetsu::Base;
use Mouse;
use Exporter qw( import );

use Type::Tiny;

our @EXPORT_OK = qw( AccessControlType TypeConstraintType );

use constant AccessControlType => Type::Tiny->new(
  name       => 'AccessControlType',
  parent     => Str,
  constraint => sub {
    my $got = shift;
    $got eq 'ro' || $got eq 'rw';
  },
);

use constant TypeConstraintType => HasMethods[qw( check get_message )];

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
  isa      => TypeConstraintType,
  required => 1,
);

no Mouse;
__PACKAGE__->meta->make_immutable;

1;
