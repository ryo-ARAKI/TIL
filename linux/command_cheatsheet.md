# Linuxの（やや複雑な）コマンドチートシート

- 前提：Linuxの一般的なコマンド（ `ls` `mv` `cp` `rm` `cd` ...）は理解しており，使えること
  - 一般的なコマンドについては [Unix/Linux コマンドリファレンス](https://kanemotilevel.com/wp/gazou/unix.pdf) などを参照のこと
- 目的：基本的なコマンドのオプションやパイプを使った組み合わせで構成されるやや複雑な（=いちいち覚えていられない）操作のチートシート

## 一般的なLinuxマシン

### `ls -lht` 細情報付きファイル一覧を，人間の読みやすい形式でのファイルサイズ及び時系列順で表示

- `ls` 当該ディレクトリ内のファイルを一覧表示
  - `-l` 長い形式で出力
  - `-h` 人間の読みやすいファイルサイズ形式で表示 `--human-readable` の略
  - `-t` ファイル更新順で表示
- `ls`のその他オプション
  - `-v` ファイル名を数字の「自然な」順で表示

### `find ./ -type f | wc -l` 現ディレクトリ内のファイル数カウント

- `find` ファイルやディレクトリの検索
  - `./` 検索起点=現在いるディレクトリ． `/` ならルートディレクトリ． `/home/hoge/huga/` のように指定すれば任意のディレクトリ内を検索できる
  - `-type f` 「ファイル」を検索． `-type d` でディレクトリを検索
- `|` 上記コマンドで出力される「ファイル名の一覧」をパイプ
- `wc` テキスト or ファイルの行数，単語数，バイト数を表示． `word count` の略
  - `-l` 行数のみを表示 `--line` と同値

### `find ./ -name "*.png" | xargs -i cp {} /path/to/dest/` 現在いるディレクトリ以下の階層から`png`の拡張子のファイルを検索し，`./hoge/`以下にコピーする

- 引数が二つあるため，`-i`オプションで`xargs`が渡す`stdin`の位置を指定する必要がある．

### `find ./ -name "*.txt" | sort | xargs cp -v --backup=numbered -f -t text/` 現ディレクトリより下の階層から `*.txt` のファイルを抽出し， `text/` ディレクトリに連番のバックアップファイルを作成しつつコピー

- 同名のファイルが `001/hoge.txt` ， `002/hoge.txt` ， `003/hoge.txt` のようにあるとき，
  - `001/hoge.txt` -> `text/hoge.txt.~1~`
  - `002/hoge.txt` -> `text/hoge.txt.~2~`
  - `003/hoge.txt` -> `text/hoge.txt`
    のようにまとめてくれる．`text/hoge.txt` を `text/hoge.txt.~3~` とリネームすれば元ディレクトリの連番とファイルの連番が対応する
- `find` ファイルやディレクトリの検索
  - `./` 検索起点=現在いるディレクトリ
  - `-name "*.txt"` `*.txt`に一致するファイル名を検索
- `| sort` `find`の検索結果を名前順にソート
- `| xargs` ソートされた検索結果を引数に取る
- `cp` ファイルのコピー
  - `-v` 途中経過を表示する． `--verbose` と同値
  - `--backup=numbered` 同名のファイルがあるとき，既存ファイルを末尾に番号をつけてバックアップ
  - `-f` 強制的に上書きする． `--force` と同値
  - `-t text/` `text` ディレクトリにコピーする． `--target-directory=text/` と同値

### `find . -name '*.png' | cpio -pdm /path/to/dest/` 現在いるディレクトリ以下の階層から `png` の拡張子ファイルを検索し， _階層を維持しつつ_ `/path/to/dest/` にコピーする

- `cpio` アーカイブファイル{への，から}ファイル{の，への}コピーをおこなう
  - `-p` コピーパスモード（ `--pass-through` ）
  - `-d` 必要に応じてディレクトリを作成（ `--make-directories` ）
  - `-m` コピーしたファイルの更新時刻をコピー元と揃える（ `--preserve-modification-time` ）

### `find . -type f -exec grep -Iq . {} \; -and -exec sed -i 's/[[:space:]]\+$//' {} +` 現在のディレクトリ以下のファイルに存在するtrailing whitespaceを全て削除する

- `exec grep -Iq . {} \;` ファイルがテキストファイルかどうかをチェックし，バイナリファイルの場合は終了コード 1 を返す
- `sed -i 's/[[:space:]]\+$//' {} +` 該当するファイルの行末の空白を削除
  - `-i` ファイルをインプレースで編集
  - `s/[[:space:]]\+$//` 正規表現を使って行末の空白を削除

### `find ./ -type f -name 'filename' -exec mv {} {}_renamed \;` 現在の階層以下から `filename` というファイルを検索し，ファイル名の末尾に `_renamed` を追加する

- cf. [How to rename multiple files using find](https://unix.stackexchange.com/a/227671)

### `rsync -n -arvt --exclude '*.bmp' user@remote_id:/remote/Dir/ /local/dir/` リモート（ `remote_id` ）にユーザー（ `user` ）でログインし， `/remote/Dir/` 以下の階層から `*bmp` 以外の拡張子のファイルを _ディレクトリ構造含めて_ ローカルの `local/dir/` にコピーする．

- `rsync` ファイルやディレクトリ環境を同期する
  - `-n` 試験モード． **実際にコピーする際はこのオプションを外す**
  - `-a` アーカイブモード． `--archive` と同値
  - `-r` ディレクトリを再帰的に処理． `--recursive` と同値
  - `-v` 動作内容を表示． `--verbose` と同値
  - `-t` タイムスタンプを保持． `--times` と同値
  - `--exclude "*.bmp"` 拡張子 `bmp` を除外する
  - `user@remote_id:/remote/Dir/` リモートマシンのアカウント名とマシン名，コピー元のディレクトリ
  - `/local/dir/` ローカルのコピー先ディレクトリ

### `du -m -d 1 | sort -rn | head -10` サイズの大きな（一階層までの）ディレクトリ Top10 を降順で表示

- ホームディレクトリで実行すること
- `du` ファイル・ディレクトリのサイズ（ディスク使用量）を表示
  - `-m` メガバイト単位で表示
    - `-h` human-readableな形式で表示，しかしこのとき，例えば `289M` -> `2.7G` のような順序での表示となってしまう...
  - `-d 1` 測定する階層の深さを 1 に指定． `--max-depth=1` と同値
- `|sort -rn` 降順でソート
- `| head -10` 最初の 10 件を表示
- `du -sch *` カレントディレクトリ直下のファイル・ディレクトリのディスク使用量と，それらの合計を表示
  - `-s` 指定したディレクトリの合計のみ表示． `--summarize` と同値
  - `-c` 全体の合計を表示． `--total` と同値
- `du -bhc /path/*.dat | tail -n 1` 指定したディレクトリ内の条件に当てはまるファイルの合計サイズを表示
  - `-b` 実際のサイズをバイト単位で表示． `--apparent-size` や `--block-size=1` と同値
  - `tail -n 1` 末尾の一行（=合計のファイルサイズ）のみを表示

### `du -h -d 1 | sort -k 2` 同じ階層にあるディレクトリのサイズ一覧をディレクトリ名でソート

- `sort -k 2`
  - 2 番目の引数（=ディレクトリ名）でソート

### `sudo rm /var/lib/apt/lists/lock && sudo rm /var/lib/dpkg/lock` ロック状態になってしまった `dpkg` の解除

- `apt` が動かないときに実行
- **TODO** `apt` と `dpkg` の関係

### `sync && sudo sysctl -w vm.drop_caches=3` メモリの開放

- `sync` メモリのバッファをディスクに書き込む
- `sysctl` カーネルパラメータを設定する
  - `-w` 変数を指定したパラメータに変更する
  - `vm.drop_caches=3` 1：ページキャッシュ，2：ダーティキャッシュと inode，3：ページキャッシュ，ダーティキャッシュと inode を破棄する

### `inkscape --export-pdf=filename.pdf --export-area-drawing --export-text-to-path filename.svg` inkspaceで作成した`svg`ファイルを，テキストをパスとしてPDFに変換

- `inkscape --export-pdf=filename.pdf --export-area-drawing --export-latex filename.svg` PDF+LaTeX（テキスト情報）に変換

### `jpegoptim --dest=compress/ -S300 hoge.jpg` `hoge.jpg`を300KBに圧縮して`./compress/`ディレクトリに保存

### `ls *.h5 | xargs du -ch | grep total$` 現在のディレクトリ中の`.h5` ファイルの総容量を表示

### `tar -czvf hoge.tgz hoge/` `hoge`/ ディレクトリ以下をgzip形式で圧縮

- `tar` アーカイブをおこなう
  - `-c`新しいアーカイブを作成する． `--create` と同値
  - `-z` ファイルをgzip形式で圧縮する． `--gzip` と同値
  - `-v`ファイルの処理状況をターミナルに出力する． `--verbose` と同値
  - `-f`アーカイブファイル名を指定する．
- 解凍の際は `tar -xzvf hoge.tgz` でファイルを展開できる．
  - `-x` ファイルを展開する． `--extract` ，あるいは `--get` と同値
  - `-C /target/dir/` で展開先のディレクトリを指定

### `pdftk original.pdf cat 1-5 output modified.pdf` PDFファイルの一部を切り出して保存

### `/bin/bash hoge` bash shellでプログラムを実行する

- fish shell で実行すると
  `The file hoge is marked as an executable but could not be run by the operating system.`
  というエラーが出るとき， `/bin/bash` と指定して実行すれば良い

### `find ./ -type f -exec grep -H "hoge" {} \;` 現在のディレクトリ以下のファイルから"hoge"を検索して一覧を表示

- `-H, --with-filename`
  - 各マッチに対するファイル名を出力

### `ffmpeg -f image2 -r 5 -i fig%3d.jpg -vb 6M test.avi` 連番画像から高画質の動画を作成

- `ffmpeg`
  - `-r` フレームレート(FPS)を指定
  - `-vb` video bitrate を設定

### `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf` PDF中の画像サイズを縮小してファイルサイズを小さくする

- `gs` ghostscript
  - `-sDEVICE=pdfwrite`
  - `-dCompatibilityLevel=1.4`
  - `-dPDFSETTINGS=/printer` PDFサイズの指定
    - `/screen` → `/ebook` → ``/printer` → `/prepress` → `/default` の順に画質が良くなる（ファイルサイズが大きくなる）
  - `-dNOPAUSE`
  - `-dQUIET`
  - `-dBATCH`

### `cut -c10-20 file.d | sort -n | uniq -c | sort -nr` `file.d`中の行の先頭から10〜20文字目で繰り返されるパターンを検知し，その頻度とともに表示する

- `cut` ファイルを読み込み，各業から指定した部分を切り出す
  - `-c10-20` 出力リスト（いまの場合，行の先頭から10〜20文字目）． `--character 10-20` と同値
- `uniq` ソートされているファイル中の重複を削除する
  - `-c` 出現回数を行の先頭に表示する． `	--count` と同値

### `screen -rd ID` アタッチ済みのセッションに再接続する

### `pip3 list --outdated | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U` python のパッケージをすべて最新版に更新する

- ` --format=freeze` オプションをつけるとエラーが出る

  ```
  ERROR: List format 'freeze' can not be used with the --outdated option.
  Defaulting to user installation because normal site-packages is not writeable
  ERROR: You must give at least one requirement to install (see "pip help install")
  ```

### TODO
