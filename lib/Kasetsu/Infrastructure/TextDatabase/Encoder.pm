package Kasetsu::Infrastructure::TextDatabase::Encoder;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use Types::Standard qw( Str );
use Cpanel::JSON::XS ();
use Kasetsu::Infrastructure::TextDatabase::DTO::Exporter;

has separator => (
  is      => 'ro',
  isa     => Str,
  default => DEFAULT_SEPARATOR,
);

sub encode {
  my ($self, $dto) = @_;
  _build_string($dto, $self->separator);
}

sub _build_string {
  my ($dto, $separator) = @_;
  my @columns = $dto->get_all_column_attributes->@*;
  my @fields  = map { $dto->$_ } map { $_->name } @columns;
  join $separator, map {
    if ( $columns[$_]->isa(NestedColumn) ) {
      my $nested_dto = $fields[$_];
      my $separator  = $columns[$_]->separator;
      _build_string($nested_dto, $separator);
    }
    elsif ( $columns[$_]->isa(JSONColumn) ) {
      my $json = Cpanel::JSON::XS->new;
      $json->convert_blessed(!!1);
      $json->encode($fields[$_]);
    }
    else {
      $fields[$_];
    }
  } 0 .. $#columns;
}

__PACKAGE__->meta->make_immutable;

1;
