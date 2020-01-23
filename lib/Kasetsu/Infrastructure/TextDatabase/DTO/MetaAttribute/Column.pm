package Kasetsu::Infrastructure::TextDatabase::DTO::MetaAttribute::Column;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { extends 'Mouse::Meta::Attribute' }

sub constraint { shift->{isa} }

1;
