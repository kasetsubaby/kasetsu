use Kasetsu::Base;
use Test2::V0;

use File::Spec;
use FindBin;
use lib File::Spec->catfile($FindBin::Bin, 'config_files');
use Kasetsu::Infrastructure::Config::GlobalVars qw( load );

subtest '設定ファイルが存在しない場合' => sub {
  my $error_message = quotemeta q{Can't locate not_exists.pl in @INC};
  like dies { load('not_exists.pl') }, qr/$error_message/;
};


subtest '設定ファイルが存在する' => sub {
  is load('kessoku_band.pl'), hash {
    field MEMBER_0 => '後藤ひとり';
    field MEMBER_1 => '伊地知虹夏';
    field MEMBER_2 => '山田リョウ';
    field MEMBER_3 => '喜多郁代';
  };
  
  is load('tmp.pl'), hash {
    field hoge => 1;
    field fuga => 2;
    field piyo => 3;
  }, '以前読み込んだ設定ファイルの内容は含まれない';
};

done_testing;
