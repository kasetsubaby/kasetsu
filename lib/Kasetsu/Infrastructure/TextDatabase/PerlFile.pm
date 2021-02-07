package Kasetsu::Infrastructure::TextDatabase::PerlFile;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::TextFile' }

use Kasetsu::Infrastructure::TextDatabase::IndexedDTOClassRecordType qw( IndexedDTOClassRecordType );

has '+record' => ( isa => IndexedDTOClassRecordType );

sub fetch_row_by_index {
  state $c = compile(Invocant, Int);
  my ($self, $index) = $c->(@_);
}

sub fetch_all_rows {
}

sub store_all_rows {
}

sub delete_row_by_index {
}

sub delete_all_rows {
}

__PACKAGE__->meta->make_immutable;

1;
