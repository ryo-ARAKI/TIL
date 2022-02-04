# LaTeX の Tips や備忘録

## `\underbrace{}`の表示がおかしい

- mathabx と mathtools パッケージを同時に使うとおかしくなる．→ 一方のみ読み込めば解決．
- [mathabx + mathtools -> extremely odd underbrace behaviour… how to fix?](https://tex.stackexchange.com/questions/117628/mathabx-mathtools-extremely-odd-underbrace-behaviour-how-to-fix)

## `siunitx`を使った単位付き数値を math 環境で使う際の最適解

```latex
\SI{9.81}{\meter/\second^2}
```

と同じ出力は

```latex
\(9.81\, \si{\meter/\second^2}\)
```

で得られる

- [The “correct” or recommended way of using siunitx in math mode](https://tex.stackexchange.com/questions/451967/the-correct-or-recommended-way-of-using-siunitx-in-math-mode)

## footnote 番号（アルファベット）や`\subfloat`の図番号がオーバーフローしてしまう

- footnote 番号をページごとにリセットする

```latex
\usepackage[perpage]{footmisc}
\renewcommand{\thefootnote}{\fnsymbol{footnote}}
```

- `subfigure`番号を適宜リセットする

```latex
\setcounter{subfigure}{0}
```

## `itemize`環境内でテキストを揃えたい

- `makebox`を使う

```latex
\begin{itemize}
  \item{\makebox[2cm][l]{$x$} is a continuous random variable.}
  \item{\makebox[2cm][l]{$f_X(x)$} is the PDF of $x$.}
  \item{\makebox[2cm][l]{$g(x)$} is a function of $x$.}
\end{itemize}
```

- [Custom alignment of text in itemized environment](https://tex.stackexchange.com/questions/147679/custom-alignment-of-text-in-itemized-environment)

## ダミー文章や図を挿入したい

### 英語：[lipsum](https://www.ctan.org/pkg/lipsum)パッケージ

```latex
# preample
\usepackage{lipsum}

# document
\lipsum[1-3]
```

### 日本語：[bxjalipsum](https://github.com/zr-tex8r/BXjalipsum)パッケージ

```latex
# preample
\usepackage{bxjalipsum}

# document
\jalipsum{iroha}  # いろは
\jalipsum{jugemu}  # 寿限無
\jalipsum[1-33]{wagahai}  # 吾輩は猫である
\jalipsum[1-4]{preamble}  # 憲法前文
\jalipsum[1-4]{hatsukoi}  # 初恋
```

### 図：[mwe](https://www.ctan.org/pkg/mwe)パッケージ

```latex
\includegraphics[width=0.6\textwidth]{example-image}
\includegraphics[width=0.6\textwidth]{example-image-16x9}
```

## `\underline{}` 中で改行できない

- 代替パッケージを使う：[下線に関するマクロ比較](http://www9.oninet.ne.jp/ohishi/tex/library/underline.pdf)

  > - `udline.sty` で定義されている `\ul` コマンド
  > - `jumoline.sty` (横組み用) で定義されている `\Underline` コマンド
  > - `jundline.sty` (横組み用) で定義されている `\jundline` コマンド
  > - `ulem.sty` で定義されている `\uline` コマンド (欧文専用) [下線拡張パッケージ udline.sty](http://minamo.my.coocan.jp/tex/udline.html)

### `ulem.sty` の導入と調節

- `sudo apt install texlive-generic-recommended` あるいは
- `sudo apt install texlive-plain-generic` （Ubuntu 20）
  で導入できる．
  - 参考：[Why am I getting missing packages in Tex](https://askubuntu.com/a/936359)
  - また， `\uline{text}` だと下線が細すぎるが `{\def\ULthickness{1pt}\uline{text}}` のようにすれば太さを変更できる．

## `empheq` 環境下で数式番号をまとめたい

- `empheq` 環境の `equation` オプションと `split` 環境を使う

```latex
\begin{empheq}[left={\vb*{f} = \empheqlbrack}, right=\empheqrbrack]{equation}
  \begin{split}
    -&\sin(x) \cos(y) \\
    +&\cos(x) \sin(y) \\
    &0
  \end{split}
\end{empheq}
```

## aligned環境下で長い方程式を改行する

- 統合を揃えつつ長い式を改行して適切にスペーシングするには `quad` を使う

```latex
\begin{empheq}{align}
  LHS of equation
    &= RHS of equation \\
    &\quad + Second line of RHS of equation
\end{empheq}
```

- 参考：[Spacing after equals sign in align](https://tex.stackexchange.com/a/212606)

## 行列，ベクトルの転置（transpose）をどう表記するか？

- `\intercal` 記号がよい

```latex
\usepackage{amssymb}
\vb*{v}^\intercal
```

- 参考：[What is the best symbol for vector/matrix transpose?](https://tex.stackexchange.com/q/30619)
  - > I would recommend the `\intercal` symbol to produce a "T" which isn't so big.
  - > Some people use a superscripted \intercal for matrix transpose: A^\intercal. (See the May 2009 comp.text.tex thread, "raising math symbols", for suggestions about altering the height of the superscript.) \top, T, and \mathsf{T} are other popular choices.

## Mathモード以外で上付き（下付き）文字を使いたい

- `\textsuperscript{hoge}` ， `\textsubscript{huga}` を使う

## Beamerで目次の表示を制御したい

- `\tableofcontents` に次のようなオプションを指定する

```latex
\tableofcontents[
  sectionstyle=show/shaded,
  subsectionstyle=show/show/shaded,
  subsubsectionstyle=show/show/show/shaded
]
```

- keyは `show, shaded, hide` の3種類
- `sectionstyle`
  1. 現在のsection
  2. それ以外のsection
- `subsectionstyle`
  1. 現在のsubsection
  2. 現在のsection中の他のsubsection
  3. 他のsection中のsubsection
- `subsubsectionstyle`
  1. 現在のsubsubsection
  2. 現在のsubsection中の他のsubsubsection
  3. 現在のsectionの他のsubsection中のsubsubsection
  4. 他のsection中のsubsection中のsubsubsection

- [Beamer: Highlighting subsubsections in TOC](https://tex.stackexchange.com/questions/231128/beamer-highlighting-subsubsections-in-toc)

## Beamerでitemize環境にアニメーションをつけたい

```latex
\begin{itemize}
  \item hoge
  \pause
  \item huga
\end{itemize}
```

のようにするとレイアウトが崩れる場合がある．

```latex
\begin{itemize}
  \item hoge
  \item<2-> huga
\end{itemize}
```

のように書けばよい．

## `REVTeX` + `biblatex` で参考文献を管理している論文をAPSに投稿する

### 前提

- 本文を記述した `.tex` ファイルに文献情報を統合したい．
  - しかし， `biblatex` パッケージで生成される `.bbl` ファイルの形式が `bibtex` で生成されるものと異なるため， `.bbl` の内容をそのまま `.tex` にコピペするのではうまくいかない．

### 解決策

- StackExchangeの[Biblatex: submitting to a journal](https://tex.stackexchange.com/a/530638)を参考にする．

1. プリアンプルで `biblatex` パッケージを読み込んだ直下に

   ```latex
   \usepackage{biblatex2bibitem}
   ```

   を記述する．
2. 文章の末尾（ `\end{document}` の直上）に

   ```latex
   \printbibitembibliography
   ```

   を記述する．
   これで，**PDFファイル**に

   ```latex
   \begin{thebibliography}{99}
    \bibitem{key1}
      bibitem information
    %
    \bibitem{key2}
      bibitem information
    %
    ...
    \end{thebibliography}
   ```

   のような `bibitem` 情報が出力される．
3. プリアンプルにある `\usepackage[...]{biblatex}` ， `\addbibsource{...}` ， `\AtEveryBibitem{...}` などの `biblatex` に関係する設定を削除する．
   また， `\printbibliography` を2. の手順で出力された `bibitem` 情報に置換する．
4. 著者名のウムラウト記号など，細かな不備を解消する．

### コメント

- おそらく，これが最も簡便に（人の手で情報を入力したり修正したりせず） `biblatex` パッケージで管理している文献情報を `.tex` ファイルに統合してAPSのサーバ上でコンパイルできるようにする方法だと思われる．

## Beamerで図を入れ替えるなどのアニメーションを入れているとき， `handout` にもそれを反映したい

```latex
\begin{frame}<handout:1-2>[label=foo]
  foo\onslide<all:2>bar
\end{frame}
```

のように書くと， `handout` でも2枚のスライドが作成される．

- 参考：[Beamer handout mode: explicitly printing "half-way" frames](https://tex.stackexchange.com/a/184136)

## Beamerの `itemize` 環境中で一部だけ異なるbulletを使いたい

プリアンプルで

```latex
\newenvironment{redenv}{\only{\setbeamercolor{local structure}{fg=red}}}{}
```

のように書き， `itemize` 環境中で次のようにすれば，一部だけbulletの色を変えることができる．

```latex
\begin{frame}
  \begin{itemize}
    \item An item
    \item<red@1-> An item with red bullet
\end{frame}
```

- 参考：[beamer: change individual bullet color in itemize list](https://tex.stackexchange.com/a/14366)

## `underbrace` 環境中で改行したい

`amsmath` パッケージの `substack` コマンドを使う

```latex
\underbrace{...}_{\substack{\text{line 1} \\ \text{line 2}}}
```

- 参考：[How can I write multiple lines in a subscript?](https://tex.stackexchange.com/a/7504)

## `\eqref` で数式を参照する

次の2つの書き方は同等な出力を与える

```latex
式~(\ref{eq:label})が拘束条件を与える．
式~\eqref{eq:label}が拘束条件を与える．
```

`\ref` の代わりに `\eqref` コマンドを使うと括弧を手入力する必要がなく，便利である．

## LaTeXdiffとgitの連携

```bash
latexdiff-vc -e utf8 -t CFONT --flatten --math-markup=2 --git --force -r HEAD^ main.tex
```

で直前のコミットとの差分が `diff-[commit hash].tex` として出力される．

- `-e utf8` 文字エンコーディングの指定
- `-t CFONT` 差分表示の指定．デフォルトだと打ち消し線と下波線での表示になるが，やや見づらいのでこちらがおすすめ
- `--flatten` `input` などで読み込んでいる別の `.tex` ファイルを正しく制御するために必要
- `--math-markup=2` 数式の差分管理の「おおらかさ」の指定．ファイルの差分が大きく `diff.tex` がうまくコンパイルできない場合はこの数値を下げるとよい．
- `-r` 差分をとる先を指定．ここでは直前のコミットを指定しているが，他にもブランチ名やコミットハッシュなどを指定できる．

- 参考
  - [Overleaf: Using Latexdiff For Marking Changes To Tex Documents](https://www.overleaf.com/learn/latex/Articles/Using_Latexdiff_For_Marking_Changes_To_Tex_Documents)
  - [にっき♪：latexdiff](<http://abenori.blogspot.com/2016/06/latexdiff.html>
  - [Gitで管理しているLaTeXのdiffをpdfで見る(TeXLive2015版)](https://nekketsuuu.github.io/entries/2017/01/27/latexdiff-vc.html)
