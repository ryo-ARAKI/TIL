# 参考文献を複数のスライドに出力する

Frame optionに `allowframebreaks` を指定すると勝手にスライドを分割してくれる．

```latex
\begin{frame}[allowframebreaks, noframenumbering]{Bibliography}
  \thispagestyle{empty}
  \printbibliography
\end{frame}
```
