package Kasetsu::Infrastructure::TextDatabase;
use Kasetsu::Base;
use Type::Params qw( compile Invocant );
use Types::Standard qw( Str Map );
use Function::Return;
use Type::Utils qw( duck_type enum );

use constant TextDatabase => duck_type([qw(
  create
  fetch
  fetch_all
  store
  store_all
  delete
  delete_all
)]);

# ログ系の場合
my @a = qw(
  append
  fetch
  fetch_all
  delete
  delete_all
);

# コマンド系の場合
my @b = qw(
);

my %NAME_TO_DATABASE = (
);

my $DatabaseNames = enum([ keys %NAME_TO_DATABASE ]);

sub get :Return(Str) {
  state $v = compile(Invocant, $DatabaseNames);
  my ($class, $name) = $v->(@_);
  $NAME_TO_DATABASE{$name};
}

1;

__END__

TextDatabase - Containter
TextDatabase::Interface
TextDatabase::SingleFile
TextDatabase::SingleFile::DTO
TextDatabase::MultipleFiles
TextDatabase::MultipleFiles::DTO
TextDatabase::DTO

TextDatabase::Decoder - テキスト行データをDTOにする処理
TextDatabase::Encoder - DTOをテキスト行データにする処理
TextDatabase::File - データベースファイルを操作するための基礎処理を提供
TextDatabase::SingleRowFile
TextDatabase::MultipleRowsFile
TextDatabase::LogFile
TextDatabase::Directory
TextDatabase::DTO
TextDatabase::DTO::...

# 機能要求
あるデータを1つ1つ別ファイルで保存しているものも,
あるデータをすべてまとめて1ファイルで保存しているものも,
同じIFで扱える

SingleFile
->fetch_row
->store_row($dto)
MultipleRowsFile
->fetch_row_of($id)
->fetch_all_rows
->store_row_of($dto)
->store_all_rows($dto_collection)
LogFile
->fetch_rows($num);
->fetch_all_rows
->append_row
->append_rows($dto_collection)
rows ではコレクションクラスのインスタンスを返す,
 配列だと自由にいじれすぎて間違ったデータをstoreする危険性が高くなるため
また各rowのidによる取得方法を統一したい
Directory
->file_of($id)
->files
my $files = Directory->files;
# やりたい
my $rows = SingleRowFileDirectory->fetch_all_rows;
SingleRowFileDircetory->store_all_rows($rows);
# コマンド系とかは?
考えてみたが一度に保存したいことはないかもしれない・・・

# 構成
- テキストデータを統一して扱うモジュール

sub get {
  my ($self, $name, $id) = @_;
  +{
    players => Directory->new(
      name => 'charalog',
      dto  => 'DTO::Player',
    ),
  };
}
