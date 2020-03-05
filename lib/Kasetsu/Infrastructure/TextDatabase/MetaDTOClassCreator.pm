package Kasetsu::Infrastructure::TextDatabase::MetaDTOClassCreator;
use Kasetsu::Base;
use Exporter qw( import );

use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';
use aliased 'Kasetsu::Infrastructure::TextDatabase::NestedColumnRole';
use Kasetsu::Infrastructure::TextDatabase::Exporter qw( MaybeClassName );
use Mouse::Meta::Class;
use Mouse::Meta::Attribute;

our @EXPORT_OK = qw( create_meta_dto_class );

sub create_meta_dto_class {
  state $c = compile(MaybeClassName, InstanceOf[Columns]);
  my ($dto_class, $columns) = $c->(@_);

  my @attributes = map {
    Mouse::Meta::Attribute->new(
      $_->name,
      is       => $_->access_control,
      isa      => $_->type_constraint,
      required => 1,
    );
  } @$columns;

  Mouse::Meta::Class->create(
    $dto_class,
    superclasses => ['Mouse::Object'],
    attributes   => \@attributes,
  );
}

1;
