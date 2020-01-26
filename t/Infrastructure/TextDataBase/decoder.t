use Kasetsu::Base;
use Test2::V0;

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

  __PACKAGE__->meta->make_immutable;
}

use aliased 'Kasetsu::Infrastructure::TextDatabase::Decoder';

my $decoder = Decoder->new(dto_class => 'Row');
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
