package Kasetsu::Infrastructure::TextDatabase;
use Kasetsu::Base;
use Kasetsu::Infrastructure::TextDatabase::Declare;

directory users => collection {
  path       './script/charalog/main';
  file_class SingleRowFile;
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::User';
    column id               => ( is => 'ro', isa => Str );
    column pass             => ( is => 'rw', isa => Str );
    column name             => ( is => 'rw', isa => Str );
    column icon             => ( is => 'rw', isa => Str );
    column force            => ( is => 'rw', isa => Int );
    column intellect        => ( is => 'rw', isa => Int );
    column leadership       => ( is => 'rw', isa => Int );
    column popular          => ( is => 'rw', isa => Int );
    column soldier_num      => ( is => 'rw', isa => Int );
    column soldier_training => ( is => 'rw', isa => Int );
    column country_id       => ( is => 'rw', isa => Int );
    column money            => ( is => 'rw', isa => Int );
    column rice             => ( is => 'rw', isa => Int );
    column contribute       => ( is => 'rw', isa => Int );
    column class            => ( is => 'rw', isa => Int );
    column weapon_index     => ( is => 'rw', isa => Int );
    column book_index       => ( is => 'rw', isa => Int );
    column loyalty          => ( is => 'rw', isa => Int );
    nested_column ability_exp => (
      is     => 'ro',
      record => record {
        dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::User::AbilityExp';
        column force      => ( is => 'rw', isa => Int );
        column intellect  => ( is => 'rw', isa => Int );
        column leadership => ( is => 'rw', isa => Int );
        column popular    => ( is => 'rw', isa => Int );
        column soldier_id => ( is => 'rw', isa => Int );
        column _unknown   => ( is => 'ro', isa => Str );
      },
    );
    column delete_turn => ( is => 'rw', isa => Int );
    column town_index  => ( is => 'rw', isa => Int );
    column _unknown    => ( is => 'ro', isa => Str );
    column host        => ( is => 'rw', isa => Int );
    column updated_at  => ( is => 'rw', isa => Int );
    column mail        => ( is => 'rw', isa => Int );
    column is_authed   => ( is => 'rw', isa => Int );
  };
};

multiple_rows_file countries => collection {
  path './script/log_file/country.cgi';
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::Country';
    attribute index => ( is => 'ro', isa => Int );
    column id                     => ( is => 'ro', isa => Int );
    column name                   => ( is => 'rw', isa => Str );
    column color_id               => ( is => 'rw', isa => Int );
    column months_after_establish => ( is => 'rw', isa => Int );
    column king_user_id           => ( is => 'ro', isa => Str );
    column command                => ( is => 'rw', isa => Str );
    nested_column user_id_of_position => (
      is     => 'ro',
      record => record {
        dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::Country::UserIDOfPosition';
        column strategist       => ( is => 'rw', isa => Str );
        column great_general    => ( is => 'rw', isa => Str );
        column cavalry_general  => ( is => 'rw', isa => Str );
        column guard_general    => ( is => 'rw', isa => Str );
        column archery_general  => ( is => 'rw', isa => Str );
        column infantry_general => ( is => 'rw', isa => Str );
      },
    );
    column _unknown => ( is => 'ro', isa => Str );
  };
};

log_file act_logs => collection {
  path './script/log_file/act_log.cgi';
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::ActLog';
    column line => ( is => 'ro', isa => Str );
  };
};

log_file admin_logs => collection {
  path './script/log_file/admin_log.cgi';
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::ActLog';
    column line => ( is => 'ro', isa => Str );
  };
};

1;

__END__
