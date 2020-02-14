package Kasetsu::Infrastructure::TextDatabase::JSONColumn;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';
BEGIN {
  extends Column;
  with 'Kasetsu::Infrastructure::TextDatabase::NestedColumnRole';
}

__PACKAGE__->meta->make_immutable;

1;
