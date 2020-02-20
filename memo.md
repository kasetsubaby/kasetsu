- Directory の実装, テスト
- Database(コンテナ) と Declare(DSL) を実装し TextDatabase で定義できるようにする
- decoder, encoder で使っているテストクラスをまとめる
- DTOクラスの自動生成機能を作成する(DTOClassCodeGenerator.pm?)
- check_com.cgi のようなディレクトリを利用したロックの仕組みを汎用的に利用する方法を考える
- 宣言とDTO以外の名前空間は適切でないので, Kasetsu::TextDatabase 以下に全て移動させる

- エラー, 未定義値の扱いどうすんの
  - 全部Eitherはしんどい...
- filelock機構からPath::Tiny抜く
