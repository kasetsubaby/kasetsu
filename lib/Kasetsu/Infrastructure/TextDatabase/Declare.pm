package Kasetsu::Infrastructure::TextDatabase::Declare;
use Kasetsu::Base;
use Exporter qw( import );
use namespace::autoclean;

use aliased 'Kasetsu::Infrastructure::TextDatabase::Database';
use aliased 'Kasetsu::Infrastructure::TextDatabase::Database';

sub database {
  state $c = compile(ClassName);
  my $klass = $c->(@_);
  state %database_of;
  $database_of{$klass} //= Database->new;
}

sub directory {
}

sub single_row_file {
}

sub multiple_rows_file {
}

sub log_file {
}

sub record {
}

sub columns {
}

sub column {
}

1;

__END__

directory name => (
  path       => '',
  file_class => '',
  record     => record(
    dto_class => '',
    columns   => columns(
      column name => (
        is => 'ro',
        isa => Str,
      ),
      column name2 => (
        is => 'ro',
        isa => Str,
      ),
    ),
  ),
);

single_row_file user => (
  path       => '',
  record     => record(
    dto_class => '',
    columns   => columns(
      column name => (
        is => 'ro',
        isa => Str,
      ),
      column name2 => (
        is => 'ro',
        isa => Str,
      ),
    ),
  ),
);
