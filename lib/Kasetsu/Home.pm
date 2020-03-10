package Kasetsu::Home;
use Kasetsu::Base;
use Exporter qw( import );

use Cwd qw( abs_path );

our @EXPORT_OK = qw( detect_home_dir );

sub search {
  my $splited_path = shift;
  die 'ホームディレクトリが見つかりません' if @$splited_path == 0;
  my $search_dir = join '/', @$splited_path;
  if ( -d "$search_dir/lib" && -d "$search_dir/.git" ) {
    $search_dir;
  }
  else {
    pop @$splited_path;
    search($splited_path);
  }
}

my sub package_name_to_pash {
  my $package_name = shift;
  $package_name =~ s!::!/!gr . '.pm';
}

sub detect_home_dir {
  my $package_name = shift // __PACKAGE__;
  my $abs_path = abs_path $INC{ package_name_to_pash($package_name) };
  my @splited_path = split m!/!, $abs_path;
  search(\@splited_path);
}

1;
