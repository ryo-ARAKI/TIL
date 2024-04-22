# GNOME shell extensionsのリスト

- [GNOME shell extensions](https://extensions.gnome.org/)
- Gnome Tweak Toolの"Extensions"から管理できるし， `gnome-shell-extension-manager` を `apt` でいれてもよい
- 設定ファイルは `~/.local/share/gnome-shell/extensions/` にあるが，単一のファイルではない（のでGist等に登録できない）

## [CoverflowAltTab](https://github.com/dmo60/CoverflowAltTab)

- Alt+Tabでのウィンドウ切り替えをより大きく表示する
- アプリアイコンのスタイル：オーバーレイ

## [Dash to Panel](https://github.com/home-sweet-gnome/dash-to-panel)

- アプリケーションランチャーとシステムトレイと融合する

### Position

- パネルを自動的に隠す：On
- Panel thickness: 64
- アプリケーションボタン：非表示
- アクティビティボタン：非表示
  - 設定アプリの「マルチタスク」で設定済
- デスクトップボタン：非表示

### Style

- アプリのアイコンにマウスを当てたときのアニメーションを有効にする：On
- 実行中インジケーターの位置：上
- 実行中インジケーターのスタイル（フォーカス）：ソリッド
- 実行中インジケーターのスタイル（非フォーカス）：ダッシュ

### Behavior

- アイコンをワークスペースごとに表示：On

## [Emoji Selector](https://github.com/maoschanz/emoji-selector-for-gnome)

- 絵文字の検索

## [RunCat](https://github.com/win0err/gnome-runcat)

- CPU負荷をグラフィカルに表示する
- Sleeping threshold = 20
- Displaying items = Character only

## [Tactile](https://t.co/jyTjYaAHvV)

- ウィンドウをタイル状に配置する
- Layout 1: 6×2（プライマリモニタ）
- Layout 2: 1×3（縦置きのサブモニタ）
- Advanced
  - Text color: #FEFAFB
  - Border color: #FED716
  - Background color: #26306B（半透明）
  - Grid size: 6×3
- 色は例えば[日本の伝統色](https://nipponcolors.com/)から探す

## おすすめ拡張機能を紹介している記事

- [Ubuntu日和：拡張機能でGNOME Shellを派手にしたり便利にしたり](https://pc.watch.impress.co.jp/docs/column/ubuntu/1440667.html)（2022）
- [GNOME42に対応したベストな 拡張機能 (失敗しないLinuxのカスタマイズ)](https://www.gustavprogress.com/gnome42%E3%81%AB%E5%AF%BE%E5%BF%9C%E3%81%97%E3%81%9F%E3%83%99%E3%82%B9%E3%83%88%E3%81%AA-%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD-%E5%A4%B1%E6%95%97%E3%81%97%E3%81%AA%E3%81%84linux%E3%81%AE%E3%82%AB/)（2022）
- [おすすめ GNOME Shell Extensions 11選](https://sy-base.com/myrobotics/ubuntu/mybest_extensions/)（2017）
