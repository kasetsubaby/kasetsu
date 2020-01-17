use v5.20;
use warnings;
use utf8;
use Path::Tiny qw( path );
use Encode qw( encode_utf8 decode );

sub collect_files {
    my $iter = path('./log_file')->iterator({ recurse => 1 });
    my @convert_files;
    while ( my $filename = $iter->() ) {
        if ( $filename =~ /(\.cgi|\.html)$/ && $filename ne __FILE__ ) {
            push @convert_files, $filename;
        }
    }
    return \@convert_files;
}

sub convert_files {
    my $files = shift;
    convert($_) for @$files;
}

sub convert {
    my $file = shift;
    my $content = decode 'sjis', path($file)->slurp;
    path($file)->spew(encode_utf8 $content);
}

my $convert_files = collect_files();
convert_files($convert_files);
