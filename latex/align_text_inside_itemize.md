# `itemize`環境内でテキストを揃える

- `makebox`を使う

```latex
\begin{itemize}
  \item{\makebox[2cm][l]{$x$} is a continuous random variable.}
  \item{\makebox[2cm][l]{$f_X(x)$} is the PDF of $x$.}
  \item{\makebox[2cm][l]{$g(x)$} is a function of $x$.}
\end{itemize}
```

- [Custom alignment of text in itemized environment](https://tex.stackexchange.com/questions/147679/custom-alignment-of-text-in-itemized-environment)
