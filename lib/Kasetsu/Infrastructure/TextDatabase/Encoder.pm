package Kasetsu::Infrastructure::TextDatabase::Encoder;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use Cpanel::JSON::XS qw( encode_json );
use Kasetsu::Infrastructure::TextDatabase::Record qw( RecordType );
use Kasetsu::Infrastructure::TextDatabase::Exporter qw( DEFAULT_SEPARATOR :column_classes_alias );

has record => (
  is       => 'ro',
  isa      => RecordType,
  required => 1,
);

has separator => (
  is      => 'ro',
  isa     => Str,
  default => DEFAULT_SEPARATOR,
);

sub encode {
  my $self = shift;
  my $dto_class = $self->record->dto_class;
  state %validator_of_dto_class;
  $validator_of_dto_class{$dto_class} //= compile(InstanceOf[$dto_class]);
  my ($dto) = $validator_of_dto_class{$dto_class}->(@_);

  _dto_to_line($dto, $self->separator, $self->record->columns);
}

sub _dto_to_line {
  my ($dto, $separator, $columns) = @_;

  my @fields = map { $dto->$_ } map { $_->name } @$columns;

  join $separator, map {
    my ($column, $field) = ($columns->[$_], $fields[$_]);

    if ( $column->isa(NestedColumn) ) {
      _dto_to_line($field, $column->separator, $column->record->columns);
    }
    elsif ( $column->isa(JSONColumn) ) {
      my %fields = map { $_ => $field->$_ } map { $_->name } $column->record->columns->@*;
      encode_json \%fields;
    }
    else {
      $field;
    }
  } 0 .. $#$columns;
}

__PACKAGE__->meta->make_immutable;

1;
