package Kasetsu::Infrastructure::TextDatabase::Directory;
use Kasetsu::Base;
use Mouse;
use Type::Tiny;
use namespace::autoclean;

use aliased 'Kasetsu::Infrastructure::TextDatabase::Column';

use constant FileClassType => Type::Tiny->new(
  name       => 'FileClassType',
  parent     => ClassName,
  constraint => sub {
    my $got = shift;
    $got->isa(Column);
  },
);

has path => (
  is       => 'ro',
  isa      => Str,
  required => 1,
);

# XXX: 拡張性が必要になれば file の Factory を作り差し替える
has file_class => (
  is       => 'ro',
  isa      => FileClassType,
  required => 1,
);

# dto_class, columns
# 上2つをまとめた何かを作る? = record class 作成
# multiple rows
# - delete も必要では
# - そもそも dto に index は必要なのか?

sub file_of {
  state $c = compile(Invocant, Str);
  my ($self, $id) = $c->(@_);
}

sub files {
}

__PACKAGE__->meta->make_immutable;

1;
