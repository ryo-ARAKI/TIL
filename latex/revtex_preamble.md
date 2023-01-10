# REVTeXなど論文執筆時の `.tex` テンプレートに追加するパッケージや設定

```latex
% ==================================================
% Add packages
% ==================================================
\usepackage{amsmath, amsfonts, amssymb, amsthm, mathtools}  % For math
\usepackage{physics, empheq}  % For advanced expressions in equations
\usepackage{hyperref}  % For links
\usepackage{graphicx}  % For figures
\graphicspath{  % Figure path =====Remove before submission=====
  {/home/raraki/github/TikZ_figures/}
}
\usepackage[labelformat=simple]{subcaption}  % For subcaption environments =====Remove before submission=====
\renewcommand\thesubfigure{(\alph{subfigure})}  % print like Fig.1(a) =====Remove before submission=====
\usepackage{tikz}  % For figure annotations =====Remove before submission=====
\usepackage[svgnames]{xcolor}  % For additional colors
\usepackage{siunitx}  % For values with units
\usepackage{tcolorbox}  % For annotations
% ==================================================
% Citation with biblatex
% ==================================================
\usepackage[
    style=authoryear,
    sorting=none,
    backend=biber,
    url=false,isbn=false,doi=false
]{biblatex}
\addbibresource{./reference.bib}
\renewbibmacro{in:}{} % Remove "in" in front of the journal name
```

- なお，参考文献は最終的に `.bbl` ファイルの内容で置換する．[submit_to_APS_with_biblatex.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/submit_to_APS_with_biblatex.md)を参照せよ．
