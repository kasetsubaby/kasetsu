package Kasetsu::Infrastructure::TextDatabase::Exporter;
use Kasetsu::Base;
use Exporter qw( import );

use Type::Tiny;
use Module::Runtime qw( is_module_name );
use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';
use aliased 'Kasetsu::Infrastructure::TextDatabase::NestedColumn';
use aliased 'Kasetsu::Infrastructure::TextDatabase::JSONColumn';

my @COLUMN_CLASSES_ALIAS = qw(
  Column
  NestedColumn
  JSONColumn
);

our @EXPORT_OK = (
  qw(
    DEFAULT_SEPARATOR
    MaybeClassName
  ),
  @COLUMN_CLASSES_ALIAS,
);

our %EXPORT_TAGS = (
  column_classes_alias => \@COLUMN_CLASSES_ALIAS,
);

use constant DEFAULT_SEPARATOR => '<>';

# Types::Standard の ClassName はロード済みのクラスである必要があるので,
# MetaDTOClassCreator で作ったクラスをチェックしたいときに使えないから作った型
use constant MaybeClassName => Type::Tiny->new(
  name       => 'MaybeClassName',
  constraint => sub {
    my $val = shift;
    is_module_name($val);
  },
);

1;
