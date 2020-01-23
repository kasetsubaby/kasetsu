package Kasetsu::Infrastructure::TextDatabase::DTO::MetaAttribute::NestedColumn;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::DTO::MetaAttribute::Column' }

use Types::Standard qw( Str );

has separator => (
  is      => 'ro',
  isa     => Str,
  default => q{,},
);

1;
