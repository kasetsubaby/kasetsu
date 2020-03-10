package Kasetsu::Infrastructure::Config::GlobalVars;
use Kasetsu::Base;
use Exporter qw( import );

use Hash::Util qw( lock_hashref );

our @EXPORT_OK = qw( load );

sub load {
  state $c = compile(Str);
  my ($filename) = $c->(@_);

  my $package_name = do {
    no warnings 'numeric';
    __PACKAGE__ . '::SandBox' . ( [] + 0 );
  };

  # グローバル変数の影響範囲をこの擬似的な匿名パッケージ内に留める
  eval <<~ "CODE";
    package $package_name;
    require '$filename';
  CODE

  die $@ if $@;

  do {
    my %config;
    no strict 'refs';
    while ( my ($name, $glob) = each %{ $package_name . '::' } ) {
      use strict 'refs';
      if ( defined $$glob ) {
        $config{$name} = $$glob;
      }
    }
    lock_hashref \%config;
  }
}

1;

__END__

=encoding utf8

=head1 NAME

Kasetsu::Infrastructure::Config::GlobalVars - グローバル変数によって記述されている設定ファイルを汚染しないように読み込む

=head1 DESCRIPTION

script/ini_file/ 内にあるような拡張子がiniだけど実態はPerlのグローバル変数で記述されている設定ファイルを読み込むモジュールです.

  use Kasetsu::Infrastructure::Config::GlobalVars qw( load );
  load('./script/ini_file/index.ini');

=cut