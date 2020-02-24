package Kasetsu::Base;
use 5.030000;
use strictures version => 2;
use warnings;
use utf8;

use parent 'Import::Base';

our @IMPORT_MODULES = (
    'utf8',
    '-bareword::filehandles',
    'strictures'      => [ version => 2 ],
    'feature'         => [':5.30'],
    '-indirect'       => ['fatal'],
    'Types::Standard' => ['-types'],
    'Type::Params'    => [qw( compile compile_named Invocant )],
);

1;
