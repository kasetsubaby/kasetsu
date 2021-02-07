package Kasetsu::Infrastructure::TextDatabase::SingleRowFile;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::TextFile' }

use Type::Params qw( validate );
use Encode qw( encode_utf8 decode_utf8 );

sub fetch_row {
  my $self = shift;
  open my $fh, '<', $self->path or die $!;
  my $line = <$fh>;
  chomp $line;
  $self->decoder->decode(decode_utf8 $line);
}

sub store_row {
  my $self = shift;
  my $dto_class = $self->record->dto_class;
  state %validator_of_dto_class;
  $validator_of_dto_class{$dto_class} //= compile(InstanceOf[$dto_class]);
  my ($row) = $validator_of_dto_class{$dto_class}->(@_);

  my $line = encode_utf8( $self->encoder->encode($row) );
  $self->data_saver->save_data([$line]);
}

__PACKAGE__->meta->make_immutable;

1;
