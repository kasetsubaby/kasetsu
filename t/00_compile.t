use strict;
use warnings;
use feature 'say';
use Test::More;

my @filenames = glob join ' ', (
    './*.pl',
    './command/*.pl',
    './entry/*.pl',
    './ini_file/*.ini',
    './map/*.pl',
    './mydata/*.pl',
);
for my $filename (@filenames) {
    require_ok $filename;
}

@filenames = glob join ' ', (
    '*.cgi',
    './entry/*.cgi',
);
for my $filename (@filenames) {
    ok !system { 'perl' } 'compile CGI', '-c', $filename;
}

done_testing;
