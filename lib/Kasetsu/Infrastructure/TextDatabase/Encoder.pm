package Kasetsu::Infrastructure::TextDatabase::Encoder;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use Cpanel::JSON::XS qw( encode_json );
use Kasetsu::Infrastructure::TextDatabase::Exporter qw( DEFAULT_SEPARATOR :column_classes_alias );

has dto_class => (
  is       => 'ro',
  isa      => ClassName,
  required => 1,
);

has columns => (
  is       => 'ro',
  isa      => ArrayRef[ InstanceOf[Column] ],
  required => 1,
);

has separator => (
  is      => 'ro',
  isa     => Str,
  default => DEFAULT_SEPARATOR,
);

has __encode_args_validator => (
  is      => 'ro',
  isa     => CodeRef,
  lazy    => 1,
  default => sub {
    my $self = shift;
    compile(Invocant, InstanceOf[ $self->dto_class ]);
  },
);

sub encode {
  my ($self, $dto) = $_[0]->__encode_args_validator->(@_);
  _dto_to_line($dto, $self->separator, $self->columns);
}

sub _dto_to_line {
  my ($dto, $separator, $columns) = @_;

  my @fields = map { $dto->$_ } map { $_->name } @$columns;

  join $separator, map {
    my ($column, $field) = ($columns->[$_], $fields[$_]);

    if ( $column->isa(NestedColumn) ) {
      _dto_to_line($field, $column->separator, $column->columns);
    }
    elsif ( $column->isa(JSONColumn) ) {
      my %fields = map { $_ => $field->$_ } map { $_->name } $column->columns->@*;
      encode_json \%fields;
    }
    else {
      $field;
    }
  } 0 .. $#$columns;
}

__PACKAGE__->meta->make_immutable;

1;
