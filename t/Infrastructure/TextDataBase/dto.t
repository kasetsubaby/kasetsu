use Kasetsu::Base;
use Test2::V0;

package Row {
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
    metaclass => NestedColumn,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has b2 => (
    metaclass => NestedColumn,
    separator => '|',
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  has c => (
    metaclass => JSONColumn,
    is        => 'ro',
    isa       => Int,
    required  => 1,
  );

  __PACKAGE__->meta->make_immutable;
}

package Row2 {
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

  __PACKAGE__->meta->make_immutable;
}

use Kasetsu::Infrastructure::TextDatabase::DTO::Exporter;

my $row = Row->new(
  a  => 1,
  b  => 2,
  b2 => 3,
  c  => 4,
);

my $cmp_type_tiny = object { prop blessed => 'Type::Tiny' };

is $row->get_all_column_attributes, array {

  item object {
    prop blessed => Column;
    call name => 'a';
    call type_constraint => $cmp_type_tiny;
  };

  item object {
    prop blessed => NestedColumn;
    call name => 'b';
    call type_constraint => $cmp_type_tiny;
    call separator => ',';
  };

  item object {
    prop blessed => NestedColumn;
    call name => 'b2';
    call type_constraint => $cmp_type_tiny;
    call separator => '|';
  };

  item object {
    prop blessed => JSONColumn;
    call name => 'c';
    call type_constraint => $cmp_type_tiny;
  };

  end;
};

my $row2 = Row2->new(a => 1);

is $row2->get_all_column_attributes, array {
  item object {
    prop blessed => Column;
    call name => 'a';
    call type_constraint => $cmp_type_tiny;
  };

  end;
};

done_testing;
