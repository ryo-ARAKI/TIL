# REVTeX + BibLaTeX で参考文献を管理している論文を APS に投稿する

## 前提

- 本文を記述した `.tex` ファイルに文献情報を統合したい．
  - しかし， BibLaTeX パッケージで生成される `.bbl` ファイルの形式が BibTeX で生成されるものと異なるため， `.bbl` の内容をそのまま `.tex` にコピペするのではうまくいかない．

## 解決策

- StackExchange の[Biblatex: submitting to a journal](https://tex.stackexchange.com/a/530638)を参考にする．

1. プリアンプルで BibLaTeX パッケージを読み込んだ直下に

   ```latex
   \usepackage{biblatex2bibitem}
   ```

   を記述する．

2. 文章の末尾（ `\end{document}` の直上）に

   ```latex
   \printbibitembibliography
   ```

   を記述する．
   これで，**PDF ファイル**に

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
   また， `\printbibliography` を 2. の手順で出力された `bibitem` 情報に置換する．
4. 著者名のウムラウト記号など，細かな不備を解消する．

## コメント

- おそらく，これが最も簡便に（人の手で情報を入力したり修正したりせず） BibLaTeX パッケージで管理している文献情報を `.tex` ファイルに統合して APS のサーバ上でコンパイルできるようにする方法だと思われる．
