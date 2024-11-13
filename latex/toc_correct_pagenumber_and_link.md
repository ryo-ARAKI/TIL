# 手動で目次に追加する項目に正しくページ番号とリンクを対応づける

ふつう， `\addcontentsline` を用いた目次への項目の手動追加は次のようにする：

```latex
\chapter*{List of Publications}  % 明示的に章として扱いたくないが
\addcontentsline{toc}{chapter}{List of publications}  % 目次には追加する
```

しかし，BibLaTeXで同様に

```latex
\printbibliography
\addcontentsline{toc}{chapter}{Bibliography}
```

とすると，目次には参考文献の **最終ページ番号** が印字されてしまう．
これは， `\printbibliography` コマンドが参考文献の出力にもなっているためである

- 参考：[Wrong page number of References in toc (scrreprt)](https://tex.stackexchange.com/a/154744)
  > the `\printbibliography` command causes the entire bibliography to print, so issuing `\addeontentsline` _after_ it will of course have the number of the last page.

さらに，これを解消しようと

```latex
\addcontentsline{toc}{chapter}{Bibliography}
\printbibliography
```

とすると，ページ番号は正しく出力されるものの `hyperref` コマンドによるリンクが **その一つ前の章/節** あてになってしまう．
これを防ぐためには，

```latex
\phantomsection
\addcontentsline{toc}{part}{Bibliography}
\printbibliography
```

のように`\phantomsection` でリンク先を調整すればよい．
これは `\printbibliography` の他に `\listoffigures` や `\listoftables` でも同じ．
