package Kasetsu::Infrastructure::TextDatabase::IndexedDTOClassRecordType;
use Kasetsu::Base;
use Exporter qw( import );

use Kasetsu::Infrastructure::TextDatabase::Record qw( RecordType );

our @EXPORT_OK = qw( IndexedDTOClassRecordType );

use constant IndexedDTOClassRecordType => do {
  my $IndexedDTOClassType = Type::Tiny->new(
    name       => 'DTOClassType',
    parent     => ClassName,
    constraint => sub {
      my $got = shift;
      $got->can('index');
    },
  );
  RecordType[$IndexedDTOClassType];
};

1;
