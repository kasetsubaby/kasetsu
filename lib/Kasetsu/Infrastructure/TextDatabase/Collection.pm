package Kasetsu::Infrastructure::TextDatabase::Collection;
use Kasetsu::Base;
use Mouse::Role;
use namespace::autoclean;

use Kasetsu::Infrastructure::TextDatabase::Record qw( RecordType );

has path => (
  is       => 'ro',
  isa      => Str,
  required => 1,
);

has record => (
  is       => 'ro',
  isa      => RecordType,
  required => 1,
);

1;
