package Kasetsu::Infrastructure::TextDatabase::Encoder;
use Kasetsu::Base;
use Mouse;
use namespace::autoclean;

use Cpanel::JSON::XS qw( encode_json );
use Kasetsu::Infrastructure::TextDatabase::Record qw( RecordType );
use Kasetsu::Infrastructure::TextDatabase::Exporter qw( DEFAULT_SEPARATOR :column_classes_alias );

has record => (
  is       => 'ro',
  isa      => RecordType,
  required => 1,
);

has separator => (
  is      => 'ro',
  isa     => Str,
  default => DEFAULT_SEPARATOR,
);

sub encode {
  my $self = shift;
  my $dto_class = $self->record->dto_class;
  state %validator_of_dto_class;
  $validator_of_dto_class{$dto_class} //= compile(InstanceOf[$dto_class]);
  my ($dto) = $validator_of_dto_class{$dto_class}->(@_);

  _dto_to_line($dto, $self->separator, $self->record->columns);
}

sub _dto_to_line {
  my ($dto, $separator, $columns) = @_;

  my @fields = map { $dto->$_ } map { $_->name } @$columns;

  join $separator, map {
    my ($column, $field) = ($columns->[$_], $fields[$_]);

    if ( $column->isa(NestedColumn) ) {
      _dto_to_line($field, $column->separator, $column->record->columns);
    }
    elsif ( $column->isa(JSONColumn) ) {
      my %fields = map { $_ => $field->$_ } map { $_->name } $column->record->columns->@*;
      encode_json \%fields;
    }
    else {
      # $field に $separator と同じ文字が含まれていると次 decode するときに正しくパースできなくなるので, エスケープ処理を行う
      my $escaped_sepatator = _to_html_special_characters($separator);
      $field =~ s/\Q$separator/$escaped_sepatator/gr;
    }
  } 0 .. $#$columns;
}

sub _to_html_special_characters {
  my $str = shift;
  state %cache;
  return $cache{$str} if exists $cache{$str};

  # https://html-css-js.com/html/character-codes/all/
  $cache{$str} = join '', map {
    my $ord = ord($_);
    die "'$_' can't transform to html special chacaters." if $ord > ord('~') || $ord < ord('!');
    '&#' . ( ord($_) - 16 ) . ';';
  } split //, $str;
}

__PACKAGE__->meta->make_immutable;

1;
