package Kasetsu::Infrastructure::TextDatabase::Directory;
use Kasetsu::Base;
use Mouse;
use Type::Tiny;
use namespace::autoclean;

use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';
use Kasetsu::Infrastructure::TextDatabase::Record qw( RecordType );

has path => (
  is       => 'ro',
  isa      => Str,
  required => 1,
);

my $FileClassType => Type::Tiny->new(
  name       => 'FileClassType',
  parent     => ClassName,
  constraint => sub {
    my $got = shift;
    $got->isa(Column);
  },
);

# XXX: 拡張性が必要になれば file の Factory を作り差し替える
has file_class => (
  is       => 'ro',
  isa      => $FileClassType,
  required => 1,
);

has record => (
  is       => 'ro',
  isa      => RecordType,
  required => 1,
);

sub file_of {
  state $c = compile(Invocant, Str);
  my ($self, $id) = $c->(@_);
}

sub files {
}

__PACKAGE__->meta->make_immutable;

1;
