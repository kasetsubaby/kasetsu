use Kasetsu::Base;
use Test2::V0;

use Type::Tiny;
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Columns';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Record' => 'Record', 'RecordType';

package Row {
  use Mouse;
  has a => (
    is       => 'ro',
    required => 1,
  );
}

package Row2 {
  use Mouse;
  has b => (
    is       => 'ro',
    required => 1,
  );
}

my $columns = Columns->new(
  contents => [
    Column->new(
      name            => 'a',
      access_control  => 'ro',
      type_constraint => Str,
    ),
  ],
);

subtest 'RecordType' => sub {
  
  subtest '型引数なし' => sub {
    my $record = Record->new(
      dto_class => 'Row',
      columns   => $columns,
    );
    is RecordType->display_name, 'Record';
    ok RecordType->check($record);
  };

  subtest '型引あり' => sub {
    
    my $type = Type::Tiny->new(
      parent     => ClassName,
      name       => 'AClassName',
      constraint => sub {
        my $class_name = shift;
        $class_name->can('a');
      },
    );
    is RecordType([$type])->display_name, 'Record[AClassName]';

    my $record = Record->new(
      dto_class => 'Row',
      columns   => $columns,
    );
    ok RecordType([$type])->check($record);

    my $record2 = Record->new(
      dto_class => 'Row2',
      columns   => $columns,
    );
    ok !RecordType([$type])->check($record2);
  };

};

done_testing;
