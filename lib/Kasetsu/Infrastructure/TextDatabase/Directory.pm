package Kasetsu::Infrastructure::TextDatabase::Directory;
use Kasetsu::Base;
use Mouse;
use Type::Tiny;
use namespace::autoclean;
BEGIN { with 'Kasetsu::Infrastructure::TextDatabase::Collection' }

use File::Spec;
use aliased 'Kasetsu::Infrastructure::TextDatabase::File';

use constant FileClassType => Type::Tiny->new(
  parent     => ClassName,
  name       => 'FileClassType',
  constraint => sub {
    my $value = shift;
    $value->isa(File);
  },
);

# XXX: 拡張性が必要になれば file の Factory を作り差し替える
has file_class => (
  is       => 'ro',
  isa      => FileClassType,
  required => 1,
);

has file_extension => (
  is      => 'ro',
  isa     => Str,
  default => 'cgi',
);

sub _make_file_path {
  my ($self, $id) = @_;
  File::Spec->catfile($self->path, $id . '.' . $self->file_extension);
}

sub file_of_id {
  state $c = compile(Invocant, Str);
  my ($self, $id) = $c->(@_);

  $self->file_class->new(
    path   => $self->_make_file_path($id),
    record => $self->record,
  );
}

sub all_exists_files {
  my $self = shift;
  opendir my $dh, $self->path or die $!;
  my $file_extension = $self->file_extension;
  my @files =
    map {
      $self->file_class->new(
        path   => $self->_make_file_path($_),
        record => $self->record,
      );
    }
    map { ($_ =~ /^(.*?)\.$file_extension$/)[0] } readdir $dh;
  \@files;
}

__PACKAGE__->meta->make_immutable;

1;
