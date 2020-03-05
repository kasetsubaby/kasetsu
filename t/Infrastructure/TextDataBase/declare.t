use Kasetsu::Base;
use Test2::V0;

package SomeDatabse {
  use Kasetsu::Base;
  use Kasetsu::Infrastructure::TextDatabase::Declare;

  directory user => collection {
    path       './script/charalog/main';
    file_class SingleRowFile;
    record {
      dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::User';
      columns {
        column id => (
          is  => 'ro',
          isa => Str,
        );
        column pass => (
          is  => 'rw',
          isa => Str,
        );
      };
    };
  };

}

use aliased 'Kasetsu::Infrastructure::TextDatabase::Database';

my $db = SomeDatabse->database;
is $db, object { prop blessed => Database };
my $user_dir = $db->get_collection('user');
is $user_dir->record->columns->@*, 2;
my $file = $user_dir->file_of_id('tmp');

done_testing;
