- MultipleRowsFile, LogFile, Directory の実装, テスト
  - MultipleRowsFile は dto_class に can('index') なクラスのクラス名しか指定できないようにする
- Database(コンテナ) と Declare(DSL) を実装し TextDatabase で定義できるようにする
- DTOクラスの自動生成機能を作成する(DTOClassCodeGenerator.pm?)
- check_com.cgi のようなディレクトリを利用したロックの仕組みを汎用的に利用する方法を考える

- filelock は　suport.pl の機構を真似る
- decoder, encoder で使っているテストクラスをまとめる
- エラー, 未定義値の扱いどうすんの
  - 全部Eitherはしんどい...
