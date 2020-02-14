use Kasetsu::Base;
use Test2::V0;
use Test2::Tools::Condition;

use Kasetsu::Infrastructure::TextDatabase::Exporter qw( :column_classes_alias );
use Mouse::Meta::Class;
use Mouse::Meta::Attribute;
use aliased 'Kasetsu::Infrastructure::TextDatabase::Encoder';

my @json_row_columns = (
  Column->new(
    name            => 'a',
    access_control  => 'ro',
    type_constraint => Int,
  ),
  Column->new(
    name            => 'b',
    access_control  => 'ro',
    type_constraint => Int,
  ),
);

my @nested_row_columns = (
  Column->new(
    name            => 'a',
    access_control  => 'ro',
    type_constraint => Int,
  ),
  JSONColumn->new(
    name            => 'b',
    access_control  => 'ro',
    type_constraint => InstanceOf['JSONRow'],
    columns         => \@json_row_columns,
  ),
);

my @columns = (
  Column->new(
    name            => 'a',
    access_control  => 'ro',
    type_constraint => Int,
  ),
  Column->new(
    name            => 'b',
    access_control  => 'ro',
    type_constraint => Int,
  ),
  NestedColumn->new(
    name            => 'c',
    access_control  => 'ro',
    type_constraint => InstanceOf['NestedRow'],
    separator       => '|',
    columns         => \@nested_row_columns,
  ),
  Column->new(
    name            => 'd',
    access_control  => 'ro',
    type_constraint => Int,
  ),
  Column->new(
    name            => 'e',
    access_control  => 'ro',
    type_constraint => Int,
  ),
  Column->new(
    name            => 'f',
    access_control  => 'ro',
    type_constraint => Str,
  ),
);

sub create_class {
  my ($class_name, $columns) = @_;
  my @attributes = map {
    Mouse::Meta::Attribute->new(
      $_->name,
      is       => $_->access_control,
      isa      => $_->type_constraint,
      required => 1,
    );
  } @$columns;
  my $class = Mouse::Meta::Class->create(
    $class_name,
    superclasses => ['Mouse::Object'],
    attributes   => \@attributes,
  );
}

my @classes = map { create_class(@$_) } (
  [ JSONRow => \@json_row_columns ],
  [ NestedRow => \@nested_row_columns ],
  [ Row => \@columns ],
);

my $row = Row->new(
  a => 1,
  b => 2,
  c => NestedRow->new(
    a => 3,
    b => JSONRow->new(
      a => 1,
      b => 2,
    ),
  ),
  d => 4,
  e => 5,
  f => 'hoge',
);
my $encoder = Encoder->new(
  dto_class => 'Row',
  columns   => \@columns,
);
my $string = $encoder->encode($row);
diag $string;
is $string, condition {
  $_ eq q{1<>2<>3|{"a":1,"b":2}<>4<>5<>hoge} || $_ eq q{1<>2<>3|{"b":2,"a":1}<>4<>5<>hoge};
};

done_testing;
