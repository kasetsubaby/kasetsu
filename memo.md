- filelock は　suport.pl の機構を真似る
- decoder, encoder で使っているテストクラスをまとめる
- DTOクラスの作成, エラーのチェックがちゃんとされないので大変そう
  - 例えば NestedColumn なのに isa が InstanceOf[A] でないとか
  - なんとかチェックできない?
    - やはりDSLか...?
- エラー, 未定義値の扱いどうすんの
  - 全部Eitherはしんどい...