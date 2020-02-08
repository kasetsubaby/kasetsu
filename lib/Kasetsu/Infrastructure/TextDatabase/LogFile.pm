package Kasetsu::Infrastructure::TextDatabase::LogFile;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::File' }

use Type::Params qw( compile Invocant );
use Types::Standard qw( Int ArrayRef InstanceOf );
use Fcntl qw( :flock );
use Encode qw( encode_utf8 decode_utf8 );
use File::ReadBackwards;

sub fetch_rows {
  state $c = compile(Invocant, Int);
  my ($self, $num) = $c->(@_);
  my $bw = File::ReadBackwards->new($self->path);
  my @rows = map {
    my $line = $bw->readline;
    $self->decoder->decode(decode_utf8 $line);
  } 0 .. $num - 1;
  \@rows;
}

sub fetch_all_rows {
  my $self = shift;
  open my $fh, '<', $self->path or die $!;
  my @rows = map { $self->decoder->decode(decode_utf8 $_) } <$fh>;
  \@rows;
}

sub append_row {
  state %checker_of_dto_class;
  $checker_of_dto_class{ $_[0]->dto_class } //= compile(Invocant, InstanceOf[ $_[0]->dto_class ]);
  my ($self, $row) = $checker_of_dto_class{ $_[0]->dto_class }->(@_);

  my $line = encode_utf8( $self->encoder->encode($row) );
  open my $fh, '>>', $self->path or die $!;
  $fh->print($line);
}

sub append_rows {
  state %checker_of_dto_class;
  $checker_of_dto_class{ $_[0]->dto_class } //= compile(Invocant, ArrayRef[ InstanceOf[ $_[0]->dto_class ] ]);
  my ($self, $rows) = $checker_of_dto_class{ $_[0]->dto_class }->(@_);

  my @lines = map { encode_utf8( $self->encoder->encode($_) ) } @$rows;
  open my $fh, '>>', $self->path or die $!;
  $fh->print(@lines);
}

1;
