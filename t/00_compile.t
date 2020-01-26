use strict;
use warnings;
use feature 'say';
use Test::More;

my @filenames = glob join ' ', (
    './script/*.pl',
    './script/command/*.pl',
    './script/entry/*.pl',
    './script/ini_file/*.ini',
    './script/map/*.pl',
    './script/mydata/*.pl',
);
for my $filename (@filenames) {
    require_ok $filename;
}

@filenames = glob join ' ', (
    './script/*.cgi',
    './script/entry/*.cgi',
);
for my $filename (@filenames) {
    ok !system { 'perl' } 'compile CGI', '-c', $filename;
}

done_testing;
