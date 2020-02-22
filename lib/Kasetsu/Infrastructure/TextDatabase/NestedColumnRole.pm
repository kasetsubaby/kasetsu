package Kasetsu::Infrastructure::TextDatabase::NestedColumnRole;
use Kasetsu::Base;
use Mouse::Role;
use namespace::autoclean;

use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Record' => 'Record', 'RecordType';

has record => (
  is       => 'ro',
  isa      => RecordType,
  required => 1,
);

has '+type_constraint' => (
  init_arg => undef,
  isa      => InstanceOf['Type::Tiny::Class'],
  lazy     => 1,
  default  => sub {
    my $self = shift;
    InstanceOf[ $self->record->dto_class ];
  },
);

1;
