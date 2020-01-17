use v5.20;
use warnings;

use FindBin;
use File::Spec;
use Plack::Builder;
use Plack::App::CGIBin;
 
my $base_dir = File::Spec->catfile($FindBin::Bin, 'script');

builder {

  enable 'Plack::Middleware::Static' => (
    path => qr!^/image|\.html$!,
    root => $base_dir,
  );

  mount '/' => Plack::App::CGIBin->new(
    root    => $base_dir,
    exec_cb => sub { 1 },
  )->to_app;

};
