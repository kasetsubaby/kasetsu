package Kasetsu::Infrastructure::TextDatabase::Record;
use Kasetsu::Base;
use Mouse;
use Exporter qw( import );

use Type::Tiny;
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';

our @EXPORT_OK = qw( RecordType );

# dto_class の型を外部から拡張したいときのために使用
# Type::Library を使わないのは meta が conflict するため
sub RecordType(;$) {
  state $c = compile(Optional[ Tuple[ InstanceOf['Type::Tiny'] ] ]);
  my ($maybe_argument) = $c->(@_);

  my $type = Type::Tiny->new(
    parent               => InstanceOf[__PACKAGE__],
    name                 => 'Record',
    name_generator       => sub {
      my ($type_name, $type_parameter) = @_;
      $type_name . '[' . $type_parameter . ']';
    },
    constraint_generator => sub {
      my $type_parameter = shift;
      sub {
        my $record = shift;
        $type_parameter->check($record->dto_class);
      };
    },
  );

  if (defined $maybe_argument) {
    $type->parameterize($maybe_argument->[0]);
  }
  else {
    $type;
  }
}

use constant MaybeClassName => StrMatch[qr/^(\w+(?:(?:::|')\w+)*)$/];

has dto_class => (
  is       => 'ro',
  isa      => MaybeClassName,
  required => 1,
);

has columns => (
  is       => 'ro',
  isa      => InstanceOf[Columns],
  required => 1,
);

no Mouse;
__PACKAGE__->meta->make_immutable;

1;
