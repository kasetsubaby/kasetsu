package Kasetsu::Infrastructure::TextDatabase::Decoder;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use Types::Standard qw( Str ClassName ArrayRef InstanceOf );
use Cpanel::JSON::XS qw( decode_json );
use Kasetsu::Infrastructure::TextDatabase::DTO::Exporter;

has dto_class => (
  is       => 'ro',
  isa      => ClassName,
  required => 1,
);

sub decode {
  my ($self, $line) = @_;
  my @fields = split /<>/, $line;
  _build_params($self->dto_class, \@fields);
}

sub _build_params {
  my ($dto_class, $fields) = @_;
  my @columns = $dto_class->get_all_column_attributes->@*;
  my %param_of_column_name =
     map {
       $columns[$_]->name => do {
         if ( $columns[$_]->isa(NestedColumn) ) {
           my $meta_attr     = $columns[$_];
           my @nested_fields = do {
             my $separator = quotemeta $meta_attr->separator;
             split /$separator/, $fields->[$_];
           };
           # もし type_constraint が InstanceOf でなければ？
           my $nested_dto_class = $columns[$_]->type_constraint->class;
           _build_params($nested_dto_class, \@nested_fields);
         }
         elsif ( $columns[$_]->isa(JSONColumn) ) {
           # もし type_constraint が InstanceOf でなければ？
           my $nested_class = $columns[$_]->type_constraint->class;
           $nested_class->new(decode_json $fields->[$_]);
         }
         else {
           $fields->[$_];
         }
       };
     }
     0 .. $#columns;
  $dto_class->new(\%param_of_column_name);
}

__PACKAGE__->meta->make_immutable;

1;
