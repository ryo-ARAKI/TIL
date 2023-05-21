# Caption中に `\footnote` を挿入する

## うまく表示されない例

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.6\textwidth]{example-image-16x9}
  \caption{
    Figure caption with footnote\footnote{Footnote to the figure caption.}.
  }
  \label{fig:example}
\end{figure}

Figure~\ref{fig:example} shows an example figure with footnote in its caption.
```

## うまく表示される例

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.6\textwidth]{example-image-16x9}
  \caption{
    Figure caption with footnote\footnotemark.
  }
  \label{fig:example}
\end{figure}

Figure~\ref{fig:example} shows an example figure with footnote in its caption.
\footnotetext{Footnote to the figure caption.}
```

## 参考リンク

- [Using \footnote in a figure's \caption](https://tex.stackexchange.com/a/10185)
