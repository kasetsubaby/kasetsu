package Kasetsu::Infrastructure::TextDatabase;
use Kasetsu::Base;
use Kasetsu::Infrastructure::TextDatabase::Declare;

directory user => collection {
  path       './script/charalog/main';
  file_class SingleRowFile;
  record {
    dto_class 'Kasetsu::Infrastructure::TextDatabase::DTO::User';
    columns {
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
          columns {
            column force      => ( is => 'rw', isa => Int );
            column intellect  => ( is => 'rw', isa => Int );
            column leadership => ( is => 'rw', isa => Int );
            column popular    => ( is => 'rw', isa => Int );
            column soldier_id => ( is => 'rw', isa => Int );
            column _unknown   => ( is => 'ro', isa => Str );
          };
        },
      );
      column delete_turn => ( is => 'rw', isa => Int );
      column town_index  => ( is => 'rw', isa => Int );
      column _unknown    => ( is => 'rw', isa => Int );
      column host        => ( is => 'rw', isa => Int );
      column updated_at  => ( is => 'rw', isa => Int );
      column mail        => ( is => 'rw', isa => Int );
      column is_authed   => ( is => 'rw', isa => Int );
    };
  };
};

1;

__END__
