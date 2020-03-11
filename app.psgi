use FindBin;
use File::Spec;
use lib File::Spec->catfile($FindBin::Bin, 'lib');
use Kasetsu::Base;

use Plack::Builder;
use Plack::App::CGIBin;

builder {

  my $base_dir = File::Spec->catfile($FindBin::Bin, 'script');

  enable 'Plack::Middleware::Static' => (
    path => qr!^/image|\.html$!,
    root => $base_dir,
  );

  mount '/' => Plack::App::CGIBin->new(
    root    => $base_dir,
    # グローバル変数利用しまくっていて永続環境では動かせないので毎回実行
    exec_cb => sub { 1 },
  )->to_app;

};
