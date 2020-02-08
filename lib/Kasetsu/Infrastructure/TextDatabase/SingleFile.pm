package Kasetsu::Infrastructure::TextDatabase::SingleFile;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::File' }

use Type::Params qw( compile Invocant );
use Types::Standard qw( InstanceOf );
use Encode qw( encode_utf8 decode_utf8 );

sub fetch_row {
  my $self = shift;
  open my $fh, '<', $self->path or die $!;
  my $line = <$fh>;
  $self->decoder->decode(decode_utf8 $line);
}

sub store_row {
  my $c = compile(Invocant, InstanceOf[ $_[0]->dto_class ]);
  my ($self, $row) = $c->(@_);
  my $line = encode_utf8( $self->encoder->encode($row) );
  $self->data_saver->save_data([$line]);
}

__PACKAGE__->meta->make_immutable;

1;
