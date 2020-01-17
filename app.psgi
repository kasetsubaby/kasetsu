use v5.20;
use warnings;

use File::Basename 'dirname';
use Plack::Builder;
use Plack::App::CGIBin;

my $base_dir = dirname __FILE__;

builder {

  enable 'Plack::Middleware::Static' => (
    path => qr!^/image!,
    root => $base_dir,
  );

  mount '/' => Plack::App::CGIBin->new(
    root    => $base_dir,
    exec_cb => sub { 1 },
  )->to_app;

};
