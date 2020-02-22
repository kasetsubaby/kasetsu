package Kasetsu::Infrastructure::TextDatabase::MultipleRowsFile;
use Kasetsu::Base;
use Mouse;
use Type::Tiny;
use namespace::autoclean;
BEGIN { extends 'Kasetsu::Infrastructure::TextDatabase::File' }

use Encode qw( encode_utf8 decode_utf8 );
use Kasetsu::Infrastructure::TextDatabase::Record qw( RecordType );

use constant IndexedDTOClassType => Type::Tiny->new(
  name       => 'DTOClassType',
  parent     => ClassName,
  constraint => sub {
    my $got = shift;
    $got->can('index');
  },
);

has '+record' => (
  isa => RecordType[IndexedDTOClassType],
);

sub fetch_row_by_index {
  state $c = compile(Invocant, Int);
  my ($self, $index) = $c->(@_);

  open my $fh, '<', $self->path or die $!;
  my $i = 0;
  while ( my $line = <$fh> ) {
    if ( $index == $i ) {
      chomp $line;
      return $self->decoder->decode(decode_utf8($line), [ index => $index ]);
    }
    $i++;
  }
  undef;
}

sub fetch_all_rows {
  my $self = shift;
  open my $fh, '<', $self->path or die $!;
  my @lines = <$fh>;
  chomp @lines;
  my @rows =
    map { $self->decoder->decode(decode_utf8($lines[$_]), [ index => $_ ]) }
    0 .. $#lines;
  \@rows;
}

sub store_row {
  my $self = shift;
  my $dto_class = $self->record->dto_class;
  state %validator_of_dto_class;
  $validator_of_dto_class{$dto_class} //= compile(InstanceOf[$dto_class]);
  my ($row) = $validator_of_dto_class{$dto_class}->(@_);

  my $rows = $self->fetch_all_rows();
  $rows->[ $row->index ] = $row;
  $self->store_all_rows($rows);
}

sub store_all_rows {
  my $self = shift;
  my $dto_class = $self->record->dto_class;
  state %validator_of_dto_class;
  $validator_of_dto_class{$dto_class} //= compile(ArrayRef[ InstanceOf[$dto_class] ]);
  my ($rows) = $validator_of_dto_class{$dto_class}->(@_);

  my @lines =
    map { "$_\n" }
    map { encode_utf8( $self->encoder->encode($_) ) } @$rows;
  $self->data_saver->save_data(\@lines);
}

sub delete_row_by_index {
  state $c = compile(Invocant, Int);
  my ($self, $index) = $c->(@_);

  my $rows = $self->fetch_all_rows();
  splice(@$rows, $index, 1) or die 'The index row doe not exists.';
  $self->store_all_rows($rows);
}

sub delete_all_rows {
  my $self = shift;
  $self->data_saver->save_data([]);
}

__PACKAGE__->meta->make_immutable;

1;
