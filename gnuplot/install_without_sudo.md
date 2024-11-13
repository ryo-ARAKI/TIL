# サーバにsudo権限無しで `gnuplot ver5.2.8` をインストールする

## 手順

### インストール

```linux
mkdir gnuplot
cd gnuplot
wget https://github.com/gnuplot/gnuplot/archive/5.2.8.tar.gz  # ソースファイルを取得
tar -zxvf 5.2.8.tar.gz  # 解凍
cd gnuplot-5.2.8
./prepare  # configureを作成
nice -n 19 ./configure --prefix=$HOME/.local  # 優先度を下げて設定ファイルを作成，インストール先を~/.local/以下に指定
nice -n 19 make  # コンパイル
nice -n 19 make install  # インストール
```

### パスの設定＆インストールできていることの確認

シェルの設定ファイルを開き

```linux
vim ~/.bashrc
```

最終行に

```bashrc
export PATH=/home/hoge/.local/bin:$PATH  # ただしhogeをユーザ名（荒木ならarakir）に変更
```

を追加して

```linux
source ~/.bashrc
gnuplot
gnuplot> plot sin(x)
```

でプロットが表示されればOK．

## 参考リンク

- [大規模ソフトウェアを手探る](https://doss.eidos.ic.i.u-tokyo.ac.jp/textbook/doss_textbook.pdf)
  - PDF．2章でgnuplotのマニュアルでのインストール手順を詳しく説明してくれている．
- [(CentOS(6.x)向け)root 権限がないサーバで必要なパッケージを自分でソースビルドして porg でパッケージ管理する](https://qiita.com/Tats_U_/items/9247c53db65ba5d55df9)
- [Ongoing development of gnuplot](http://www.gnuplot.info/development/)
  - `configure` を作るために `./prepare` を叩く必要があることはここで分かる（なかなか分からなくて時間を溶かした...）
  - gnuplot のバージョンによっては圧縮ファイルを解凍した段階で `configure` がある．
