# REVTeXなど論文執筆時の `.tex` テンプレートに追加するパッケージや設定

プリアンブルに以下をコピペする：

```latex
% ==================================================
% Add packages
% ==================================================
\usepackage{amsmath, amsfonts, amssymb, amsthm, mathtools, ascmac}  % For math
\usepackage{physics, empheq}  % For advanced expressions in equations
\usepackage{hyperref}  % For links
\hypersetup{  % =====Remove before submission=====
  colorlinks=true,
  linkcolor=magenta,
  citecolor=blue,
  urlcolor=cyan,
  pdftitle={PDF title},
  pdfauthor={ARAKI Ryo}
}
\usepackage{graphicx}  % For figures
\graphicspath{  % Figure path =====Remove before submission=====
  {/path/to/figures/}
}
\usepackage[labelformat=simple]{subcaption}  % For subcaption environments =====Remove before submission=====
\renewcommand\thesubfigure{~(\alph{subfigure})}  % print like Fig.~1~(a) =====Remove before submission=====
\usepackage{tikz}  % For figure annotations =====Remove before submission=====
\usepackage[svgnames]{xcolor}  % For additional colors
\usepackage{siunitx}  % For values with units
\usepackage[most]{tcolorbox}  % For annotations
% ==================================================
% Citation with biblatex =====Remove before submission=====
% ==================================================
\usepackage[
  style=ext-authoryear,
  backend=biber,
  date=year,
  articlein=false, isbn=false, doi=false, url=false,
  backref=true
]{biblatex}
\addbibresource{./reference.bib}
\usepackage{/home/raraki/.config/LaTeX/mystyle_biblatex}
```

また，参考文献の出力は

```latex
% Create the reference section using BibLaTeX:
\printbibliography
```

でおこなう．
なお，参考文献は最終的に `.bbl` ファイルの内容で置換する．
[submit_to_APS_with_biblatex.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/submit_to_APS_with_biblatex.md)を参照せよ．
