package Kasetsu::Infrastructure::TextDatabase::HugeLogFile;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::File' }

use Encode qw( encode_utf8 decode_utf8 );
use File::ReadBackwards;

sub fetch_rows {
  state $c = compile(Invocant, Int);
  my ($self, $num) = $c->(@_);

  my $bw = File::ReadBackwards->new($self->path);
  my @rows = map {
    my $line = $bw->readline;
    chomp $line;
    $self->decoder->decode(decode_utf8 $line);
  } 0 .. $num - 1;
  $bw->close;
  \@rows;
}

sub fetch_all_rows {
  my $self = shift;
  my $bw = File::ReadBackwards->new($self->path);
  my @rows;
  while ( my $line = $bw->readline ) {
    chomp $line;
    push @rows, $self->decoder->decode(decode_utf8 $line);
  }
  $bw->close;
  \@rows;
}

sub append_row {
  my $self = shift;
  my $dto_class = $self->record->dto_class;
  state %validator_of_dto_class;
  $validator_of_dto_class{$dto_class} //= compile(InstanceOf[$dto_class]);
  my ($row) = $validator_of_dto_class{$dto_class}->(@_);

  my $line = encode_utf8( $self->encoder->encode($row) ) . "\n";
  open my $fh, '>>', $self->path or die $!;
  $fh->print($line);
}

sub append_rows {
  my $self = shift;
  my $dto_class = $self->record->dto_class;
  state %validator_of_dto_class;
  $validator_of_dto_class{$dto_class} //= compile(ArrayRef[ InstanceOf[$dto_class] ]);
  my ($rows) = $validator_of_dto_class{$dto_class}->(@_);

  my @lines =
    map { "$_\n" }
    map { encode_utf8( $self->encoder->encode($_) ) } @$rows;
  open my $fh, '>>', $self->path or die $!;
  $fh->print(@lines);
}

1;
