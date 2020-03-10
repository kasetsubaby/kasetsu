use Kasetsu::Base;
use Test2::V0;

use Kasetsu::Home qw( detect_home_dir );

# テストどう書こう・・・
use aliased 'Kasetsu::Infrastructure::Config::GlobalVars';
diag detect_home_dir(GlobalVars);
ok 1;

done_testing;
