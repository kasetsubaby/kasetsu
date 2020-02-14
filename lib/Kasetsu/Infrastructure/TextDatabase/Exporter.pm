package Kasetsu::Infrastructure::TextDatabase::Exporter;
use Kasetsu::Base;
use Exporter qw( import );

use constant DEFAULT_SEPARATOR => '<>';

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
  ),
  @COLUMN_CLASSES_ALIAS,
);

our %EXPORT_TAGS = (
  column_classes_alias => \@COLUMN_CLASSES_ALIAS,
);

1;
