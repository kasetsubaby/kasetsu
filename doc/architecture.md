# アーキテクチャ

## 思想
- 軽量DDDで開発を進める
  - 具体的には MVC + UseCase
  - https://zenn.dev/mpyw/articles/ce7d09eb6d8117
- アクターを意識して責務ごとにモジュールを分割する

## 移植方針
- デフォルトの三国志NETの仕様を可能な限り引き継ぐ
  - 明らかに機能していないコードは削除してok
- デフォルトの三国志NETのコードと一緒に運用できるようにする
  - データのフォーマットは変更しない
- pl はできるだけライブラリ化

## 構造

### View
表示に関する責務を担当する層。

```
Kasetsu::View::Model - 表示するデータ構造を表現する
Kasetsu::View::Render - テンプレートのレンダリングを行う
template/
```

### Controller
View と UseCase の間のやりとりをする層。
リクエストに応じて UseCase を呼び出し、UseCase から受け取った値を ViewModel に加工し template に渡してレンダリングする。

```
Kasetsu::Controller::${Actor} - コントローラのロジック(HTTPリクエストを受け取りそれに基づいてServiceからデータを取得しそれをViewに加工する層), 基本CGIファイルにベタ書きだけどページ間で共有したいものなどあれば・・・
```


### UseCase
各ユースケースの実装がある。
アクターごとに大まかに分類している。

Read系の処理では Infrastructure 層からデータを取得しそのデータを Controller にそのまま返す。
Write系の処理では Infrastructure 層から取得したデータをドメイン用に変換してビジネスロジックを実行する。


```
Kasetsu::UseCase::Visitor - ユーザーでなくても見れるページのロジック, 単なるウェブページの訪問者が閲覧できるページのロジック
Kasetsu::UseCase::Register - 登録, 建国処理 登録済みのユーザーとはアクターが違うと考え分割
Kasetsu::UseCase::Player - (ログイン済みの)ユーザーから操作されたりみれるところ。Playerは更に細かく分けると部隊長や国の上層職みたいな分け方ができるので、それらはどうする？(こちらが用意するロジックでないと判定できないアクターでは層はわけない、で良さそう?)
Kasetsu::UseCase::WorldUpdater - 更新処理、もともとindex.cgiでやっていたことの実行、具体的には半年ごとの都市ステータスの変化やプレイヤーのコマンド実行とか
Kasetsu::UseCase::Admin - 管理機能(これもさらに機能がわかれるかもしれない, デベロッパーツール, ユーザ管理ツール, サービス管理ツール, データ(通常プランナーとかだけど三Nだとデベロッパーと同じかも)作成ツールなど)
Kasetsu::UseCase::History - ゲームの記録をするため(史記など)のロジック
Kasetsu::UseCase::Debug - デバッグ機能
Kasetsu::UseCase::Core - アクターによって振る舞いが変化しない機能だったり、各アクターと共有したい振る舞いを集める場所
```

### Infrastructure
コードと外部とのやりとりをする層。
具体的にはデータの読み取り/書き込みをしたりAPIを叩いたりする。

#### TextDataBase
各データをDTOとして共通のインターフェースで扱えるモジュール。
