package Kasetsu::Type::Utils::Generics;
use Kasetsu::Base;
use Exporter qw( import );

our @EXPORT_OK = qw( generics T );
our %EXPORT_TAGS = ( all => \@EXPORT_OK );

use List::Util qw( all );
use constant TypeParameterType => 'Kasetsu::Type::Utils::Generics::TypeParameterType';

sub T {
  TypeParameterType
}

sub generics {
  state $c = do {
    my $NamedOptionsType = Dict[
      class_name => ClassName,
      attributes => HashRef[ InstanceOf['Type::Tiny'] ],
    ];
    compile(Str, slurpy $NamedOptionsType);
  };
  my ($name, $args) = $c->(@_);
  my ($class_name, $template_of) = $args->@{qw( class_name attributes )};

  sub {
    state $c = compile(ArrayRef);
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
