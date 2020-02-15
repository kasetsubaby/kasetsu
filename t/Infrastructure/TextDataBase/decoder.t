use Kasetsu::Base;
use Test2::V0;

use Mouse::Meta::Class;
use Mouse::Meta::Attribute;
use Kasetsu::Infrastructure::TextDatabase::Exporter qw( :column_classes_alias );
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Decoder';

my $json_row_columns = Columns->new(
  contents => [
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
  ]
);

my $nested_row_columns = Columns->new(
  contents => [
    Column->new(
      name            => 'a',
      access_control  => 'ro',
      type_constraint => Int,
    ),
    JSONColumn->new(
      name            => 'b',
      access_control  => 'ro',
      type_constraint => InstanceOf['JSONRow'],
      columns         => $json_row_columns,
    ),
  ],
);

my $columns = Columns->new(
  contents => [
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
      columns         => $nested_row_columns,
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
  ],
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
  [ JSONRow   => $json_row_columns ],
  [ NestedRow => $nested_row_columns ],
  [ Row       => $columns ],
);

my $decoder = Decoder->new(
  dto_class => 'Row',
  columns   => $columns,
);
my $row = $decoder->decode('1<>2<>3|{"a":1,"b":2}<>4<>5<>hoge');

is $row, object {
  prop blessed => 'Row';
  call a => 1;
  call b => 2;
  call c => object {
    prop blessed => 'NestedRow';
    call a => 3;
    call b => object {
      prop blessed => 'JSONRow';
      call a => 1;
      call b => 2;
    };
  };
  call d => 4;
  call e => 5;
  call f => 'hoge';
};

done_testing;
