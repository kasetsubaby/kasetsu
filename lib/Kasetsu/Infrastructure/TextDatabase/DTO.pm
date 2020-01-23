package Kasetsu::Infrastructure::TextDatabase::DTO;
use Kasetsu::Base;
use Mouse::Role;
use namespace::autoclean;

use aliased 'Kasetsu::Infrastructure::TextDatabase::DTO::MetaAttribute::Column';

sub get_all_column_attributes {
  my $class = ref $_[0] || $_[0];
  state %meta_attrs_of_class_name;
  $meta_attrs_of_class_name{$class} //=
    [ grep { $_->isa(Column) } $class->meta->get_all_attributes ];
}

1;
