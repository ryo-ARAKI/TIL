# Frametitle 中で右揃えする

以下のように書くとうまくいかない（二行目が右揃えにならない）：

```LaTeX
\begin{frame}{
  Title of the frame\\
  \vspace{-0.5\baselineskip}\hfill {\scriptsize Some remark on the slide}
}
\end{frame}
```

以下のように `\hspace{0pt plus 1 filll}` を挿入するとうまくいく：

```LaTeX
\begin{frame}{
  Title of the frame\\
  \vspace{-0.5\baselineskip} \hspace{0pt plus 1 filll} {\scriptsize Some remark on the slide}
}
\end{frame}
```

- 参考：[Using \hfill in a beamer \frametitle in the wuerzburg theme](https://tex.stackexchange.com/a/118234)
