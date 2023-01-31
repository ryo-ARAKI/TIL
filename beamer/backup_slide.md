# 補遺スライドを作成する

`\backupbegin` と `\backupend` で挟めばよい

```latex
\backupbegin

% ===========================================
\section*{Supplemental slides}
% ===========================================

\begin{frame}[noframenumbering]
  \thispagestyle{empty}
  \centering
  \begin{beamercolorbox}
    [wd=\textwidth, center, sep=2pt, rounded=true, shadow=false]{frametitle}
    \insertsection
  \end{beamercolorbox}
\end{frame}


% ++++++++++++++++++++++++++++++++++++++++++++++++++
\subsection{subsection title}
% ++++++++++++++++++++++++++++++++++++++++++++++++++

\begin{frame}{\insertsubsection}
  このスライド番号は N+1/N （ただし N は本文のスライド枚数）と表示される
\end{frame}

\backupend
```
