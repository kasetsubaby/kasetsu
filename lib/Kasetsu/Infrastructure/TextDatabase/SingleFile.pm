package Kasetsu::Infrastructure::TextDatabase::SingleFile;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::File' }

use Type::Params qw( validate );
use Encode qw( encode_utf8 decode_utf8 );

sub fetch_row {
  my $self = shift;
  open my $fh, '<', $self->path or die $!;
  my $line = <$fh>;
  $self->decoder->decode(decode_utf8 $line);
}

has __store_row_args_validator => (
  is      => 'ro',
  isa     => CodeRef,
  lazy    => 1,
  default => sub {
    my $self = shift;
    compile(Invocant, InstanceOf[ $self->dto_class ]);
  },
);

sub store_row {
  my ($self, $row) = $_[0]->__store_row_args_validator->(@_);
  my $line = encode_utf8( $self->encoder->encode($row) );
  $self->data_saver->save_data([$line]);
}

__PACKAGE__->meta->make_immutable;

1;
