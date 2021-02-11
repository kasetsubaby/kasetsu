package Kasetsu::Type::Utils::Generics::TypeParameterType;
use Kasetsu::Base;
use parent 'Type::Tiny';
use Exporter qw( import );

our @EXPORT_OK = qw( T );

use Carp qw( croak );

sub T {
  state $c = compile(Str, slurpy Dict[ optional => Optional[Bool] ]);
  my ($type_parameter_id, $maybe_options) = $c->(@_);
  __PACKAGE__->new(
    type_parameter_id => $type_parameter_id,
    defined $maybe_options ? %$maybe_options : (),
  );
}

sub new {
  state $c = do {
    my $Args = Dict[
      type_parameter_id => Str,
      optional          => Optional[Bool],
      slurpy,
    ];
    compile(Invocant, slurpy $Args);
  };
  my ($class, $args) = $c->(@_);

  my $self = $class->SUPER::new(%$args, name => 'TypeParameterType');
  $self->{$_} = $args->{$_} for qw( type_parameter_id optional );
  $self;
}

sub type_parameter_id { shift->{type_parameter_id} }
sub optional { shift->{optional} }

sub constraint {
  croak q{Can not use this type for type constraint. (only used to identify type parameter.) };
}

1;
