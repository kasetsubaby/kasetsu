package Kasetsu::Type::Utils::Generics::AlternativeTypes;
use Kasetsu::Base;
use Type::Library -base;
use Type::Tiny::Class;
use Type::Tiny::Role;

my $meta = __PACKAGE__->meta;

$meta->add_type({
  name                 => 'InstanceOf',
  parent               => Object,
  constraint_generator => sub {
    my $class_name = shift;
    return $meta->get_type('InstanceOf') unless defined $class_name;

    Type::Tiny::Class->new(
      class        => $class_name,
      display_name => "InstanceOf[$class_name]",
    );
  },
});

$meta->add_type({
  name                 => 'ConsumerOf',
  parent               => Object,
  constraint_generator => sub {
    my $role_name = shift;
    return $meta->get_type('ConsumerOf') unless defined $role_name;

    Type::Tiny::Role->new(
      role         => $role_name,
      display_name => "ConsumerOf[$role_name]",
    );
  },
});

$meta->make_immutable;

1;

__END__

=encoding utf8

=head1 NAME

Kasetsu::Type::Utils::Generics::AlternativeTypes

=head1 DESCRIPTION

Types::Standard::InstanceOf, Types::Standard::ConsumerOf とほぼ同等の型チェックができる型を提供します。

Types::Standard::InstanceOf, Types::Standard::ConsumerOf と Kasetsu::Type::Utils::Generics::TypeParameterType を組み合わせて利用できないため、作られました。
これらの型は type constraint を型引数として受け取ると型引数をそのまま返してしまうという仕様があります。
例えば InstanceOf[ T(0) ], ConsumerOf[ T(0) ] という型を作ると T(0), T(0) となってしまいます。
これでは型テンプレートとして利用できないため、同等の機能を提供する型を独自実装して利用するようにしました。


=cut
