package Kasetsu::Infrastructure::TextDatabase::TextFile::Decoder;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use Cpanel::JSON::XS qw( decode_json );
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';
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

sub decode {
  state $c = compile(Invocant, Str, Optional[ArrayRef]);
  my ($self, $line, $extra) = $c->(@_);
  _line_to_dto($line, quotemeta $self->separator, $self->record, $extra);
}

sub _line_to_dto {
  my ($line, $separator, $record, $maybe_extra) = @_;

  my @fields = split /$separator/, $line;
  my $columns = $record->columns;
  my %params_of_column_name = map {
    my ($column, $field) = ($columns->[$_], $fields[$_]);

    $column->name => do {
      if ( $column->isa(NestedColumn) ) {
        _line_to_dto($field, quotemeta $column->separator, $column->record);
      }
      elsif ( $column->isa(JSONColumn) ) {
        $column->record->dto_class->new(decode_json $field);
      }
      else {
        $field;
      }
    };
  } 0 .. $#$columns;

  $record->dto_class->new(%params_of_column_name, defined $maybe_extra ? @$maybe_extra : ());
}

__PACKAGE__->meta->make_immutable;

1;
