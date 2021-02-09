use Kasetsu::Base;
use Test2::V0;
use Kasetsu::Type::Utils::Generics qw( generics );

package Column {
  use Kasetsu::Base;
  use Mouse;
  has name => (
    is       => 'ro',
    isa      => Str,
    required => 1,
  );
}

package Columns {
  use Kasetsu::Base;
  use Mouse;
  has contents => (
    is       => 'ro',
    isa      => ArrayRef[ InstanceOf['Column'] ],
    required => 1,
  );
}

my $ColumnsType = generics Columns => 'Columns', ['contents'];
my $ParameterizeType = $ColumnsType->([ ArrayRef[InstanceOf['Column']] ]);

my $columns = Columns->new(contents => [ Column->new(name => '雫') ]);
ok $ParameterizeType->check($columns);

done_testing;
