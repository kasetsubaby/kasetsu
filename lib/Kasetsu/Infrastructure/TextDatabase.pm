package Kasetsu::Infrastructure::TextDatabase;
use Kasetsu::Base;
use Kasetsu::Infrastructure::TextDatabase::Declare;

use Kasetsu::Infrastructure::Config::GlobalVars qw( load );
use File::Spec;
use Kasetsu::Home qw( detect_home_dir );

my $INDEX_INI = load( File::Spec->catfile( detect_home_dir(), qw( script ini_file index.ini ) ) );

directory users => collection {
  path       $INDEX_INI->{CHARA_DATA};
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
      },
    );
    column delete_turn => ( is => 'rw', isa => Int );
    column town_index  => ( is => 'rw', isa => Int );
    column _unknown    => ( is => 'ro', isa => Any );
    column host        => ( is => 'rw', isa => Str );
    column updated_at  => ( is => 'rw', isa => Int );
    column mail        => ( is => 'rw', isa => Str );
    column is_authed   => ( is => 'rw', isa => Int );
  };
};

single_row_file access_counter => collection {
  path 'log_file/counter.cgi';
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::AccessCounter';
    column num => ( is => 'rw', isa => Int );
  };
};

# ユーザ行動ログ
log_file act_logs => collection {
  path      'log_file/act_log.cgi';
  max_lines 800;
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::ActLog';
    column line => ( is => 'ro', isa => Str );
  };
};

# 解雇された人のブラックリスト
multiple_rows_file black_list => collection {
  path 'log_file/black_list.cgi';
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::BlackList';
    attribute index => ( is => 'ro', isa => Int );
    column 'user_id'       => ( is => 'ro', isa => Str );
    column 'country_index' => ( is => 'ro', isa => Str );
    column 'user_name'     => ( is => 'ro', isa => Str );
  };
};

multiple_rows_file weapons => collection {
  path $INDEX_INI->{ARM_LIST};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::Weapon';
    attribute index => ( is => 'ro', isa => Int );
    column name       => ( is => 'ro', isa => Str );
    column price      => ( is => 'ro', isa => Int );
    column power      => ( is => 'ro', isa => Num );
    column _unknown_1 => ( is => 'ro', isa => Str );
    column _unknown_2 => ( is => 'ro', isa => Str );
    column _unknown_3 => ( is => 'ro', isa => Str );
    column _unknown_4 => ( is => 'ro', isa => Str );
    column _unknown_5 => ( is => 'ro', isa => Str );
  };
};

multiple_rows_file books => collection {
  path $INDEX_INI->{PRO_LIST};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::Book';
    attribute index => ( is => 'ro', isa => Int );
    column name       => ( is => 'ro', isa => Str );
    column price      => ( is => 'ro', isa => Int );
    column power      => ( is => 'ro', isa => Num );
    column _unknown_1 => ( is => 'ro', isa => Str );
    column _unknown_2 => ( is => 'ro', isa => Str );
    column _unknown_3 => ( is => 'ro', isa => Str );
    column _unknown_4 => ( is => 'ro', isa => Str );
    column _unknown_5 => ( is => 'ro', isa => Str );
  };
};

multiple_rows_file countries => collection {
  path $INDEX_INI->{COUNTRY_LIST};
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

# ゲーム時刻
single_row_file game_date => collection {
  path 'log_file/date_count.cgi';
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::GameDate';
    column elapsed_year => ( is => 'rw', isa => Int );
    column month        => ( is => 'rw', isa => Int );
    column time         => ( is => 'rw', isa => Int );
  };
};

# 国アピールメッセージ
multiple_rows_file countries_appeal_messages => collection {
  path $INDEX_INI->{COUNTRY_MES};
  record {

    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::CountryAppealMessage';
    attribute index => ( is => 'ro', isa => Int );
    column new_country_id   => ( is => 'ro', isa => Str );
    column country_color_id => ( is => 'ro', isa => Str );
  };
};

# 建国リスト
multiple_rows_file founded_countries => collection {
  path $INDEX_INI->{COUNTRY_MES};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::FoundedCountry';
    attribute index => ( is => 'ro', isa => Int );
    column country_id           => ( is => 'ro', isa => Int );
    column country_name         => ( is => 'rw', isa => Str );
    column country_color_id     => ( is => 'rw', isa => Str );
    column _unknown_2           => ( is => 'rw', isa => Str );
    column country_king_user_id => ( is => 'ro', isa => Str );
    column _unknown_3           => ( is => 'rw', isa => Str );
    column _unknown_4           => ( is => 'ro', isa => Str );
    column _unknown_5           => ( is => 'ro', isa => Str );
  };
};

# 守備データ
multiple_rows_file towns_defenders => collection {
  path $INDEX_INI->{DEF_LIST};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::TownDefender';
    attribute index => ( is => 'ro', isa => Int );
    column user_id         => ( is => 'ro', isa => Str );
    column user_name       => ( is => 'ro', isa => Str );
    column town_index      => ( is => 'ro', isa => Str );
    column _unknown        => ( is => 'ro', isa => Str );
    column user_country_id => ( is => 'ro', isa => Int );
  };
};

for my $pair (
  [ towns         => $INDEX_INI->{TOWN_LIST} ],
  [ initial_towns => $INDEX_INI->{F_TOWN_LIST} ]
) {
  my ($name, $path) = @$pair;

  multiple_rows_file $name => collection {
    path $path;
    record {
      dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::Town';
      attribute index => ( is => 'ro', isa => Int );
      column name         => ( is => 'ro', isa => Str );
      column country_id   => ( is => 'rw', isa => Str );
      column farmer       => ( is => 'rw', isa => Int );
      column farm         => ( is => 'rw', isa => Int );
      column business     => ( is => 'rw', isa => Int );
      column wall         => ( is => 'rw', isa => Int );
      column farm_max     => ( is => 'rw', isa => Int );
      column business_max => ( is => 'rw', isa => Int );
      column wall_max     => ( is => 'rw', isa => Int );
      column loyalty      => ( is => 'rw', isa => Int );
      column x            => ( is => 'ro', isa => Int );
      column y            => ( is => 'ro', isa => Int );
      column price        => ( is => 'rw', isa => Num );
      column wall_power   => ( is => 'rw', isa => Int );
      column technology   => ( is => 'rw', isa => Int );
      column farmer_max   => ( is => 'rw', isa => Int );
      # 隣接都市のID
      # このデータがなくでも座標から都市間の距離求めて移動できる都市を判定できるので不要にできる
      column next_town_index_0 => ( is => 'ro', isa => Int );
      column next_town_index_1 => ( is => 'ro', isa => Int );
      column next_town_index_2 => ( is => 'ro', isa => Int );
      column next_town_index_3 => ( is => 'ro', isa => Int );
      column next_town_index_4 => ( is => 'ro', isa => Int );
      column next_town_index_5 => ( is => 'ro', isa => Int );
      column next_town_index_6 => ( is => 'ro', isa => Int );
      column next_town_index_7 => ( is => 'ro', isa => Int );
    };
  };
}

# 現在参加しているプレーヤリスト
multiple_rows_file online_users => collection {
  path $INDEX_INI->{GUEST_LIST};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::OnlineUser';
    attribute index => ( is => 'ro', isa => Int );
    column onlined_at      => ( is => 'ro', isa => Num );
    column user_name       => ( is => 'ro', isa => Str );
    column user_country_id => ( is => 'ro', isa => Str );
    column user_town_index => ( is => 'ro', isa => Str );
  };
};

# local_rule.cgi (国法)
multiple_rows_file countries_rules => collection {
  path $INDEX_INI->{LOCAL_LIST};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::CountryRule';
    attribute index => ( is => 'ro', isa => Int );
    column user_id            => ( is => 'ro', isa => Str );
    column no                 => ( is => 'ro', isa => Int );
    column message            => ( is => 'ro', isa => Str );
    column user_icon          => ( is => 'ro', isa => Int );
    column user_name          => ( is => 'ro', isa => Str );
    column _unknown_1         => ( is => 'ro', isa => Str );
    column wrote_at_formatted => ( is => 'ro', isa => Str );
    column country_color_id   => ( is => 'ro', isa => Int );
    column country_id         => ( is => 'ro', isa => Int );
    column _unknown_2         => ( is => 'ro', isa => Str );
  };
};

# 国会議室
multiple_rows_file countries_bbs => collection {
  path $INDEX_INI->{BBS_LIST};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::CountryBBS';
    attribute index => ( is => 'ro', isa => Int );
    column title              => ( is => 'ro', isa => Str );
    column message            => ( is => 'ro', isa => Str );
    column user_icon          => ( is => 'ro', isa => Int );
    column user_name          => ( is => 'ro', isa => Str );
    column _unknown           => ( is => 'ro', isa => Str );
    column wrote_at_formatted => ( is => 'ro', isa => Str );
    column country_color_id   => ( is => 'ro', isa => Int );
    column country_id         => ( is => 'ro', isa => Int );
    column type               => ( is => 'ro', isa => Enum[0, 1] ); # thread or reply
    column no                 => ( is => 'ro', isa => Int );
    column maybe_thread_id    => ( is => 'ro', isa => Int );
  };
};

# マップログ
log_file map_log => collection {
  path      $INDEX_INI->{MAP_LOG_LIST};
  max_lines $INDEX_INI->{MAP_LOG_LIST_MAX_LINES};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::MapLog';
    column line => ( is => 'ro', isa => Str );
  };
};

# 史記
log_file history_log => collection {
  path      $INDEX_INI->{MAP_LOG_LIST2};
  max_lines $INDEX_INI->{MAP_LOG_LIST2_MAX_LINES};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::HistoryLog';
    column line => ( is => 'ro', isa => Str );
  };
};

# 手紙
log_file letters => collection {
  path      $INDEX_INI->{MESSAGE_LIST};
  max_lines $INDEX_INI->{MES_MAX};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::Letter';
    column type              => ( is => 'ro', isa => Str ); # country_id or receiver_id or 333(都市宛) or 111(部隊宛)
    column sender_id         => ( is => 'ro', isa => Str );
    column sender_town_index => ( is => 'ro', isa => Str );
    column sender_name       => ( is => 'ro', isa => Str );
    column message           => ( is => 'ro', isa => Str );
    column receiver_name     => ( is => 'ro', isa => Str );
    column send_at_formatted => ( is => 'ro', isa => Str );
    column sender_icon       => ( is => 'ro', isa => Int );
    column sender_country_id => ( is => 'ro', isa => Int );
    column sender_unit_id    => ( is => 'ro', isa => Str );
  };
};

# 密書
log_file offer_letters => collection {
  path      $INDEX_INI->{MESSAGE_LIST2};
  max_lines $INDEX_INI->{MES_MAX};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::OfferLetter';
    column receiver_id       => ( is => 'ro', isa => Str );
    column sender_id         => ( is => 'ro', isa => Str );
    column sender_town_index => ( is => 'ro', isa => Str );
    column sender_name       => ( is => 'ro', isa => Str );
    column message           => ( is => 'ro', isa => Str );
    column receiver_name     => ( is => 'ro', isa => Str );
    column send_at_formatted => ( is => 'ro', isa => Str );
    column sender_icon       => ( is => 'ro', isa => Int );
    column sender_country_id => ( is => 'ro', isa => Int );
  };
};

# 負荷防止のためのhost記録ファイル
multiple_rows_file recently_accessed_hosts => collection {
  path 'log_file/stop.cgi';
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::RecentlyAccessedHost';
    attribute index => ( is => 'ro', isa => Int );
    column accessed_at => ( is => 'ro', isa => Int );
    column host        => ( is => 'ro', isa => Str );
  };
};

# unit_list.cgi (部隊)
multiple_rows_file units => collection {
  path $INDEX_INI->{UNIT_LIST};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::Unit';
    attribute index => ( is => 'ro', isa => Int );
    column id               => ( is => 'ro', isa => Str );
    column name             => ( is => 'rw', isa => Str );
    column country_id       => ( is => 'rw', isa => Int );
    column is_member_leader => ( is => 'rw', isa => Bool );
    column member_id        => ( is => 'ro', isa => Str );
    column member_name      => ( is => 'rw', isa => Str );
    column member_icon      => ( is => 'rw', isa => Int );
    column message          => ( is => 'rw', isa => Str );
    column can_join         => ( is => 'rw', isa => Bool );
  };
};

# 管理画面行動ログ
log_file admin_logs => collection {
  path      $INDEX_INI->{ADMIN_LIST};
  max_lines $INDEX_INI->{ADMIN_LIST_MAX_LINES};
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::ActLog';
    column line => ( is => 'ro', isa => Str );
  };
};

1;

__END__
