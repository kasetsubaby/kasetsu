use Kasetsu::Base;
use Test2::V0;
use Test2::Tools::Condition;

package Row {
  use Mouse;
  BEGIN { with 'Kasetsu::Infrastructure::TextDatabase::DTO' }
  use Kasetsu::Infrastructure::TextDatabase::DTO::Exporter;

  use Types::Standard qw( Int Str InstanceOf );

  has a => (
    metaclass => Column,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has b => (
    metaclass => Column,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has c => (
    metaclass => NestedColumn,
    separator => '|',
    is        => 'ro',
    isa       => InstanceOf['NestedRow'],
    required  => 1,
  );

  has d => (
    metaclass => Column,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has e => (
    metaclass => Column,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has f => (
    metaclass => Column,
    is        => 'ro',
    isa       => Str,
    required  => 1,
  );

  __PACKAGE__->meta->make_immutable;
}

package NestedRow {
  use Mouse;
  BEGIN { with 'Kasetsu::Infrastructure::TextDatabase::DTO' }
  use Kasetsu::Infrastructure::TextDatabase::DTO::Exporter;

  use Types::Standard qw( Int InstanceOf );

  has a => (
    metaclass => Column,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has b => (
    metaclass => JSONColumn,
    is        => 'ro',
    isa       => InstanceOf['JSONRow'],
    required  => 1,
  );

  __PACKAGE__->meta->make_immutable;
}

package JSONRow {
  use Mouse;
  BEGIN { with 'Kasetsu::Infrastructure::TextDatabase::DTO' }
  use Kasetsu::Infrastructure::TextDatabase::DTO::Exporter;

  use Types::Standard qw( Int );

  has a => (
    metaclass => Column,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has b => (
    metaclass => Column,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  sub TO_JSON {
    my $self = shift;
    +{ %$self };
  }

  __PACKAGE__->meta->make_immutable;
}

use aliased 'Kasetsu::Infrastructure::TextDatabase::Decoder';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Encoder';

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
my $encoder = Encoder->new;
my $string  = $encoder->encode($row);
is $string, condition {
  $_ eq q{1<>2<>3|{"a":1,"b":2}<>4<>5<>hoge} || $_ eq q{1<>2<>3|{"b":2,"a":1}<>4<>5<>hoge};
};

done_testing;
