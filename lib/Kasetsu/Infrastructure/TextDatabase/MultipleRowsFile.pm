package Kasetsu::Infrastructure::TextDatabase::MultipleRowsFile;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::File' }

use Type::Params qw( compile Invocant );
use Types::Standard qw( Int ArrayRef InstanceOf );
use Fcntl qw( :flock );
use Encode qw( encode_utf8 decode_utf8 );

sub fetch_row_of {
  state $c = compile(Invocant, Int);
  my ($self, $id) = $c->(@_);
  open my $fh, '<', $self->path or die $!;
  my $i = 0;
  while ( my $line = <$fh> ) {
    if ( $id == $i ) {
      return $self->decoder->decode(decode_utf8($line), +{ index => $i });
    }
    $i++;
  }
  undef;
}

sub fetch_all_rows {
  my $self = shift;
  open my $fh, '<', $self->path or die $!;
  my @lines = <$fh>;
  my @rows = map { $self->decoder->decode(decode_utf8($lines[$_]), +{ index => $_ }) } 0 .. $#lines;
  \@rows;
}

sub store_row_of {
  state %checker_of_dto_class;
  $checker_of_dto_class{ $_[0]->dto_class } //= compile(Invocant, InstanceOf[ $_[0]->dto_class ]);
  my ($self, $row) = $checker_of_dto_class{ $_[0]->dto_class }->(@_);

  my $rows = $self->fetch_all_rows();
  $rows->[ $row->id ] = encode_utf8( $self->encoder->encode($row) );
  $self->store_all_rows($rows);
}

sub store_all_rows {
  state %checker_of_dto_class;
  $checker_of_dto_class{ $_[0]->dto_class } //= compile(Invocant, ArrayRef[ InstanceOf[ $_[0]->dto_class ] ]);
  my ($self, $rows) = $checker_of_dto_class{ $_[0]->dto_class }->(@_);

  my @lines =
    map { "$_\n" }
    map { encode_utf8( $self->encoder->encode($_) ) } @$rows;
  $self->data_saver->save_data(\@lines);
}

__PACKAGE__->meta->make_immutable;

1;
