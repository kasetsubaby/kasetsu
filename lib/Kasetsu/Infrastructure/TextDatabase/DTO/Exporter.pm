package Kasetsu::Infrastructure::TextDatabase::DTO::Exporter;
use Kasetsu::Base;
use Exporter qw( import );

use Types::Standard ();

use aliased 'Kasetsu::Infrastructure::TextDatabase::DTO::MetaAttribute::ID';
use aliased 'Kasetsu::Infrastructure::TextDatabase::DTO::MetaAttribute::Column';
use aliased 'Kasetsu::Infrastructure::TextDatabase::DTO::MetaAttribute::NestedColumn';
use aliased 'Kasetsu::Infrastructure::TextDatabase::DTO::MetaAttribute::JSONColumn';

use constant DEFAULT_SEPARATOR => '<>';

use constant DTOClassType =>
  Types::Standard::ClassName->where(sub { $_->does('Kasetsu::Infrastructure::TextDatabase::DTO') });

our @EXPORT = qw(
  Column
  NestedColumn
  JSONColumn
  DEFAULT_SEPARATOR
  DTOClassType
);

1;
