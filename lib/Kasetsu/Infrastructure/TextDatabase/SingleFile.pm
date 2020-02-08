package Kasetsu::Infrastructure::TextDatabase::SingleFile;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::File' }

use Type::Params qw( compile Invocant );
use Types::Standard qw( InstanceOf );
use Fcntl qw( :flock );
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
  my $temp = $self->path . $$ . int( rand( 2 ** 31 ) );
  open my $fh, '>', $temp or die $!;
  flock($fh, LOCK_EX) or die $!;
  $fh->print($line);
  $fh->close or die $!;
  rename($temp, $self->path);
}

__PACKAGE__->meta->make_immutable;

1;
