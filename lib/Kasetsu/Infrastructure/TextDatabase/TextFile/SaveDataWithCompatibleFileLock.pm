package Kasetsu::Infrastructure::TextDatabase::TextFile::SaveDataWithCompatibleFileLock;
use Kasetsu::Base;
use Mouse;
use Types::Standard qw( InstanceOf ArrayRef Str );
use Type::Params qw( compile Invocant );
use namespace::autoclean;

use List::Util qw( any );
use Path::Tiny qw( path );

has path_str => (
  is       => 'ro',
  isa      => Str,
  init_arg => 'path',
  required => 1,
);

has path => (
  is       => 'ro',
  isa      => InstanceOf['Path::Tiny'],
  lazy     => 1,
  default  => sub {
    my $self = shift;
    path($self->path_str);
  },
  init_arg => undef,
);

has lockfile_path => (
  is      => 'ro',
  isa     => InstanceOf['Path::Tiny'],
  lazy    => 1,
  default => sub {
    my $self = shift;
    $self->path->parent->child($self->path->basename . '.tmp');
  },
);

has tmpfile_path => (
  is      => 'ro',
  isa     => InstanceOf['Path::Tiny'],
  lazy    => 1,
  default => sub {
    my $self = shift;
    $self->path->parent->child($self->path->basename . '.dmy.tmp');
  },
);

sub tmpfiles {
  my $self = shift;
  [ $self->lockfile_path, $self->tmpfile_path ];
}

sub is_locked {
  my $self = shift;

  my @tmpfiles = $self->tmpfiles->@*;
  my @remains_files = grep {
    my $path = $_;
    any { $_ eq $path } @tmpfiles;
  } $self->path->parent->children;

  return !!0 unless @remains_files;

  my $mtime   = $self->lockfile_path->exists ? $self->lockfile_path->stat->mtime : 0;
  my $at_last = time - $mtime - 10;
  if ($mtime && 0 < $at_last) {
    $self->unlock();
    0;
  }
  else {
    1;
  }
}

sub save_data {
  state $c = compile(Invocant, ArrayRef[Str]);
  my ($self, $lines) = $c->(@_);

  die "ファイルがロックされています。" if $self->is_locked();

  eval {
    $self->lockfile_path->touch();
    for ($self->tmpfile_path) {
      $_->touch();
      $_->chmod(0666);
      $_->spew(@$lines);
      $_->move($self->path);
    }
    $self->lockfile_path->remove();
  };
  if (my $e = $@) {
    $self->unlock();
    die $e;
  }
}

sub unlock {
  my $self = shift;
  for my $path ($self->tmpfiles->@*) {
    $path->remove();
  }
}

1;

__END__

=encoding utf8

=head1 NAME

  Kasetsu::Infrastructure::TextDatabase::FileLock;

=head1 DESCRIPTION

  ファイルにロックをかけつつ保存する機能を提供するモジュールです。
  元のコードの suport.pl のファイル保存&ロック機能(sub SAVE_DATA) と同等の機能をそなえ、また同時に運用してもデータロストが発生しないような仕組みになっています。

  元のコードを利用している部分がなくなったのであれば、 flock を利用するように実装を変えるべきだと思います。

=cut
