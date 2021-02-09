package Kasetsu::Type::Utils::Generics;
use Kasetsu::Base;
use Exporter qw( import );

use List::Util qw( all );

our @EXPORT_OK = qw( generics );

sub generics {
  state $c = compile(Str, ClassName, ArrayRef[ Str | Tuple[ Str, Dict[ optional => Bool ] ] ]);
  my ($name, $class_name, $attributes) = $c->(@_);

  sub {
    state $c = compile(ArrayRef[ InstanceOf['Type::Tiny'] ]);
    my ($type_parameters) = $c->(@_);

    Type::Tiny->new(
        parent               => InstanceOf[$class_name],
        name                 => $name,
        name_generator       => sub {
          my ($type_name, @type_parameters) = @_;
          $type_name . '[' . join(', ', @type_parameters) . ']';
        },
        constraint_generator => sub {
          my @type_parameters = @_;
          sub {
            my $object = shift;
            all {
              my ($attribute, $type_parameter) = ($attributes->[$_], $type_parameters[$_]);
              ref $attribute eq 'ARRAY' && $attribute->[1]{optional}
                ? $type_parameter->check($object->${ \$attribute->[0] })
                : $type_parameter->check($object->$attribute);
            } 0 .. $#$attributes;
          };
        },
      )
      ->parameterize(@$type_parameters);
  };
}

1;
