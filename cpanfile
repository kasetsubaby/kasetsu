requires 'perl', '5.030001';
requires 'strictures';
requires 'Import::Base';
requires 'aliased';
requires 'namespace::autoclean';
requires 'Type::Tiny', '== 1.008001';
requires 'Function::Return', '== 0.07';
requires 'Mouse', '== 2.5.9';
requires 'Exception::Tiny', '== 0.2.1';
requires 'CGI', '== 4.45';

on test => sub {
  requires 'Test2::Suite', '== 0.000127';
};

on develop => sub {
  requires 'Plack', '== 1.0047';
  requires 'CGI::Emulate::PSGI', '== 0.23';
  requires 'CGI::Compile', '== 0.23';
};
