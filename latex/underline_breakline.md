# `\underline` 環境中で改行する

- 代替パッケージを使う：[下線に関するマクロ比較](http://www9.oninet.ne.jp/ohishi/tex/library/underline.pdf)

  > - `udline.sty` で定義されている `\ul` コマンド
  > - `jumoline.sty` (横組み用) で定義されている `\Underline` コマンド
  > - `jundline.sty` (横組み用) で定義されている `\jundline` コマンド
  > - `ulem.sty` で定義されている `\uline` コマンド (欧文専用) [下線拡張パッケージ udline.sty](http://minamo.my.coocan.jp/tex/udline.html)

## `ulem.sty` の導入と調節

- `sudo apt install texlive-generic-recommended` あるいは
- `sudo apt install texlive-plain-generic` （Ubuntu 20）
  で導入できる．
  - 参考：[Why am I getting missing packages in Tex](https://askubuntu.com/a/936359)
  - また， `\uline{text}` だと下線が細すぎるが `{\def\ULthickness{1pt}\uline{text}}` のようにすれば太さを変更できる．
