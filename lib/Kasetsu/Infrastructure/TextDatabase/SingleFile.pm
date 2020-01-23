package Kasetsu::Infrastructure::TextDatabase::SingleFile;
use Kasetsu::Base;
use Mouse;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::File' }

sub fetch_row {
}

sub store_row {
}

__PACKAGE__->meta->make_immutable;

1;
