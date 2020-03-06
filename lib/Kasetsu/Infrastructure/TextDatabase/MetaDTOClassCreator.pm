package Kasetsu::Infrastructure::TextDatabase::MetaDTOClassCreator;
use Kasetsu::Base;
use Exporter qw( import );

use Kasetsu::Infrastructure::TextDatabase::Column qw( AccessControlType TypeConstraintType );
use Kasetsu::Infrastructure::TextDatabase::Exporter qw( MaybeClassName );
use Mouse::Meta::Class;
use Mouse::Meta::Attribute;

our @EXPORT_OK = qw( create_meta_dto_class );

sub create_meta_dto_class {
  state $AttributeParams = Dict[
    name => Str,
    is   => AccessControlType,
    isa  => TypeConstraintType,
  ];
  state $c = compile(MaybeClassName, ArrayRef[$AttributeParams]);
  my ($dto_class, $attributes_params) = $c->(@_);

  my @attributes =
    map { Mouse::Meta::Attribute->new($_->{name} => $_->%{qw( is isa )}) } @$attributes_params;

  Mouse::Meta::Class->create(
    $dto_class,
    superclasses => ['Mouse::Object'],
    attributes   => \@attributes,
  );
}

1;
