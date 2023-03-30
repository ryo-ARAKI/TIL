# 論文雑誌テンプレートを使って arXiv にプレプリントを投稿する際の注意点

## Journal of Fluid Mechanics のテンプレート `jfm.cls`

- 行番号を表示しない
  - `documentclass` から `lineno` オプションを削除する
- Footer を表示しない
  - `\corresp{}` コマンドによる email の表示を削除する
  - `jfm.cls` の footer 定義を削除（下記参照）
- `.bbl` ファイルを使って参考文献を表示する
  - `\bibliography{}` で `.bib` ではなく `.bbl` ファイル名を指定する

`jfm.cls` で footer が定義されている部分

```latex
\def\absfooterflag{\footerflagdefns{Abstract must not spill onto p.2}}%

\def\pagelimitfooter{\bgroup%
\ifnum\c@page=4\relax%
\footerflagdefns{Focus on Fluids articles must not exceed this page length}%
\else%
\ifnum\c@page=10\relax%
\footerflagdefns{Rapids articles must not exceed this page length}%
\fi\fi%
\egroup}%

\def\ps@headings{\let\@mkboth\markboth
  \def\@oddhead{\hfil{\itshape\@shorttitle}\hfil\llap{\thepage}}%
  \def\@evenhead{\rlap{\thepage}\hfil\itshape\@shortauthor\hfil}%
  \def\@oddfoot{}%
  \def\@evenfoot{\pagelimitfooter}%
  \def\sectionmark##1{\markboth{##1}{}}%
  \def\subsectionmark##1{\markright{##1}}%
}

...

\hbox to \textwidth{{\fboxsep0pt\fbox{\parbox{\textwidth}{\par\vskip2.7pc\centerline{Banner appropriate to article type will appear here in typeset article}\par\vskip2.7pc}}}}
}}
  \def\@evenhead{\@j@urnal \hfil\llap{\thepage}}%
  \def\@oddfoot{\absfooterflag}%
  \def\@evenfoot{\absfooterflag}%
  \def\sectionmark##1{}%
  \def\subsectionmark##1{}%
}
```

を以下のように修正する

```latex
\def\ps@headings{\let\@mkboth\markboth
  \def\@oddhead{\hfil{\itshape\@shorttitle}\hfil\llap{\thepage}}%
  \def\@evenhead{\rlap{\thepage}\hfil\itshape\@shortauthor\hfil}%
  \def\@oddfoot{}%
  \def\@evenfoot{}%
  \def\sectionmark##1{\markboth{##1}{}}%
  \def\subsectionmark##1{\markright{##1}}%
}

...

\hbox to \textwidth{{\fboxsep0pt\fbox{\parbox{\textwidth}{\par\vskip2.7pc\centerline{Banner appropriate to article type will appear here in typeset article}\par\vskip2.7pc}}}}
}}
  \def\@evenhead{\@j@urnal \hfil\llap{\thepage}}%
  \def\@oddfoot{}%
  \def\@evenfoot{}%
  \def\sectionmark##1{}%
  \def\subsectionmark##1{}%
}
```

## IOP Publishing のテンプレート `iopart.cls`

`equation*` 環境の上書きを無効化するために

````latex
\@namedef{equation*}{\[}
\@namedef{endequation*}{\]}
````

の二行をコメントアウトする
