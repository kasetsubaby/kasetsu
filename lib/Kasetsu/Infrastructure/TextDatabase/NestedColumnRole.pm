package Kasetsu::Infrastructure::TextDatabase::NestedColumnRole;
use Kasetsu::Base;
use Mouse::Role;
use namespace::autoclean;
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';

has '+type_constraint' => (
  isa => InstanceOf['Type::Tiny::Class'],
);

has columns => (
  is       => 'ro',
  isa      => InstanceOf[Columns],
  required => 1,
);

has dto_class => (
  is      => 'ro',
  isa     => ClassName,
  lazy    => 1,
  default => sub {
    my $self = shift;
    $self->type_constraint->class;
  },
);

1;