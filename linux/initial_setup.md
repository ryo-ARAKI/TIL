# Ubuntu日本語Remixをインストール後におこなう初期設定

実行環境

```linux
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.3 LTS
Release:	22.04
Codename:	jammy
```

- システムを更新して再起動する

```linux
sudo apt -y update
sudo apt -yV upgrade
sudo apt -yV dist-upgrade
sudo apt -yV autoremove
sudo apt autoclean
sudo shutdown -r now
```

- 必要なソフトウェアを追加する・不要なソフトウェアを削除する

```linux
sudo apt -y install git
sudo apt -y install curl
sudo apt -y install vim
sudo apt -y install evince  # PDFビューワ
sudo apt -y install ffmpeg  # 画像処理
sudo apt -y install terminator  # かっこいいターミナルエミュレータ
sudo apt -y install fish  # モダンなシェル
sudo apt -y install ubuntu-restricted-extras  # フォント・動画再生用コーデック
sudo apt install -y fonts-ipafont && fc-cache -fv  # IPAフォント
sudo apt -y install gnome-tweaks  # 詳細設定
sudo apt -y install gnome-shell-extension-manager  # Gnome Extensions
sudo apt -y purge thunderbird*  # デフォルトのメーラー
```

- ホームディレクトリ下の日本語ディレクトリを英語に変換する

```linux
$ LANG=C xdg-user-dirs-gtk-update
```

- 日本語入力のため `fcitx-mozc` をインストールし，設定する

```linux
$ sudo apt -y install fcitx-mozc
$ im-config -n fcitx
$ fcitx-configtool mozc &
```

- 時計合わせのサーバをNICTへ変更する

```linux
$ sudo sed -i 's/#NTP=/NTP=ntp.nict.jp/g' /etc/systemd/timesyncd.conf
```

- デスクトップにゴミ箱を表示する

```linux
$ gsettings set org.gnome.shell.extensions.ding show-trash true
```

- デスクトップ背景を単色にする
  - HTMLカラーコードは例えば[日本の伝統色](https://nipponcolors.com/)から探す

```linux
$ gsettings set org.gnome.desktop.background picture-uri ''
$ gsettings set org.gnome.desktop.background color-shading-type 'solid'
$ gsettings set org.gnome.desktop.background primary-color '#268785'  # 青碧
```

- 設定アプリ
  - スタイル：暗い（色は好みで）
  - マルチタスク：ホットコーナーを有効化する
  - 電源管理：バッテリー残量を表示する
- Gnome-tweaks
  - ウィンドウ：ウィンドウ操作キー：Alt
  - ウィンドウ：ホバーでフォーカスを当てる
  - キーボードとマウス：追加のレイアウトオプション：Caps LockをControlとして扱う
  - キーボードとマウス：マウスクリックのエミュレーション：無効
  - トップバー：曜日
  - フォント：インターフェースのテキスト：IPA Pゴシック Regular 11
  - フォント：ドキュメントのテキスト：IPA Pゴシック Regular 11
  - フォント：等幅テキスト：Monospace Regular 13
  - フォント：レガシーなウィンドウタイトル：IPA Pゴシック Bold 11

## To Do

- Chrome
- VSCode
  - snap版ではなくdeb版
  - 設定ファイルを見直す
- GitHub
  - sshでなくGitHub CLIで設定する
- ssh

## 参考にしたページ

- [金子邦彦研究室：Ubuntu 22.04 のインストール直後の設定](https://www.kkaneko.jp/tools/ubuntu/ubuntu_setup.html)
- [@karaage0703：Ubuntuをちょっと使いやすくする設定集](https://qiita.com/karaage0703/items/705f1b750c486f00d554)
