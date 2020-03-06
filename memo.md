- Declareでファイル宣言
- gitignoreしっかり設定
- 実装
- decoder, encoder で使っているテストクラスをまとめる
- check_com.cgi のようなディレクトリを利用したロックの仕組みを汎用的に利用する方法を考える
- 宣言とDTO以外の名前空間は適切でないので, Kasetsu::TextDatabase 以下に全て移動させる

- エラー, 未定義値の扱いどうすんの
  - 全部Eitherはしんどい...
- filelock機構からPath::Tiny抜く
