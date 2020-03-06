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
requires 'Cpanel::JSON::XS', '== 4.18';
requires 'File::ReadBackwards', '== 1.05';
requires 'Path::Tiny', '== 0.112';
requires 'Module::Runtime', '== 0.016';
requires 'Class::Load', '== 0.25';

on test => sub {
  requires 'Test2::Harness', '== 0.001099';
  requires 'Test2::Suite', '== 0.000127';
  requires 'Test2::Tools::Condition', '== 0.03';
  requires 'Test::MockTime', '== 0.17';
};

on develop => sub {
  requires 'Plack', '== 1.0047';
  requires 'CGI::Emulate::PSGI', '== 0.23';
  requires 'CGI::Compile', '== 0.23';
  requires 'Data::Printer', '== 0.40';
};
