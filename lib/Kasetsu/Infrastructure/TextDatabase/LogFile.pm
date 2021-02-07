package Kasetsu::Infrastructure::TextDatabase::LogFile;
use Kasetsu::Base;
use Mouse;
use Type::Tiny;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::TextFile' }

use Encode qw( encode_utf8 decode_utf8 );

has max_lines => (
  is       => 'ro',
  isa      => Int,
  required => 1,
);

sub fetch_rows {
  state $c = compile(Invocant, Int);
  my ($self, $num) = $c->(@_);

  open my $fh, '<', $self->path or die $!;
  my $count = 0;
  my @rows;
  while (my $line = <$fh>) {
    chomp $line;
    push @rows, $self->decoder->decode(decode_utf8 $line);
    last if ++$count == $num;
  }
  \@rows;
}

sub fetch_all_rows {
  my $self = shift;
  open my $fh, '<', $self->path or die $!;
  my @lines = <$fh>;
  chomp @lines;
  my @rows =
    map { $self->decoder->decode(decode_utf8 $lines[$_]) }
    0 .. $#lines;
  \@rows;
}

sub _store_all_rows {
  my $self = shift;
  my $dto_class = $self->record->dto_class;
  state %validator_of_dto_class;
  $validator_of_dto_class{$dto_class} //= compile(ArrayRef[ InstanceOf[$dto_class] ]);
  my ($rows) = $validator_of_dto_class{$dto_class}->(@_);

  splice @$rows, $self->max_lines;

  my @lines =
    map { "$_\n" }
    map { encode_utf8( $self->encoder->encode($_) ) } @$rows;
  $self->data_saver->save_data(\@lines);
}

sub append_row {
  my $self = shift;
  my $dto_class = $self->record->dto_class;
  state %validator_of_dto_class;
  $validator_of_dto_class{$dto_class} //= compile(InstanceOf[$dto_class]);
  my ($row) = $validator_of_dto_class{$dto_class}->(@_);

  my $rows = $self->fetch_all_rows();
  unshift @$rows, $row;
  $self->_store_all_rows($rows);
}

sub append_rows {
  my $self = shift;
  my $dto_class = $self->record->dto_class;
  state %validator_of_dto_class;
  $validator_of_dto_class{$dto_class} //= compile(ArrayRef[ InstanceOf[$dto_class] ]);
  my ($append_rows) = $validator_of_dto_class{$dto_class}->(@_);

  my $rows = $self->fetch_all_rows();
  unshift @$rows, reverse @$append_rows;
  $self->_store_all_rows($rows);
}

__PACKAGE__->meta->make_immutable;

1;
