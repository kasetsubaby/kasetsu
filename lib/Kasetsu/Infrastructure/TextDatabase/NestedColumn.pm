package Kasetsu::Infrastructure::TextDatabase::NestedColumn;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';
BEGIN {
  extends Column;
  with 'Kasetsu::Infrastructure::TextDatabase::NestedColumnRole';
}

has separator => (
  is      => 'ro',
  isa     => Str,
  default => q{,},
);

__PACKAGE__->meta->make_immutable;

1;
