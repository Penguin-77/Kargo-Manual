# conf.py for Sphinx + LaTeX + PDF

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Kargo硬件用户手册'
copyright = '2026, JAKA'
author = 'JAKA'
release = 'V01-α'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinx_simplepdf',
    'myst_parser',
    'sphinx_design',
]

source_suffix = {
 '.rst': 'restructuredtext',
 '.txt': 'restructuredtext',
 '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
master_doc = 'index'

# 自动编号
numfig = True
numfig_secnum_depth = 1

# -- HTML -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/Logo1.png'

numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码块 %s',
    'section': '节 %s'
}

# 中文搜索
html_search_language = 'zh'
html_search_options = {
    'type': 'jieba',
    'lang': 'zh_CN'
}

# 查找图片偏好
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = ['image/svg+xml', 'image/png', 'image/gif', 'image/jpeg']

from sphinx.builders.latex import LaTeXBuilder
LaTeXBuilder.supported_image_types = ['application/pdf', 'image/png', 'image/jpeg']

# -- LaTeX -------------------------------------------------

latex_engine = 'xelatex'

latex_documents = [
    ('index', 'KargoManual.tex', 'Kargo硬件用户手册',
     author, 'manual'),
]

latex_table_style = ['longtable', 'booktabs']

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'figure_align': 'H',
    'maketitle': r'\input{cover.tex}',
    'atendofbody': r'\input{backcover.tex}',
    'fncychap': r'\usepackage[Sonny]{fncychap}',
    'extraclassoptions': 'openany,oneside',

    # 1. 字体设置：解决 "Missing character" 的基础
    'fontpkg': r'''
\usepackage{xeCJK}
\setCJKmainfont{Noto Sans CJK SC}
\setCJKsansfont{Noto Sans CJK SC}
\setCJKmonofont{Noto Sans Mono CJK SC}

\setmainfont{FreeSerif}
\setsansfont{FreeSans}
\setmonofont{FreeMono}
''',

    'preamble': r'''
\usepackage[titles]{tocloft}
\hypersetup{unicode=true}
\usepackage{xeCJK}
\usepackage{xeCJKfntef}
\usepackage{graphicx}
\usepackage{float}
\usepackage{colortbl}

% 强制全局中文字体，防止部分环境回退
\setCJKmainfont{Noto Sans CJK SC}

% ===== 页面边距与页眉空间分配 =====
\usepackage{geometry}
\geometry{
    left=25mm,
    right=25mm,
    top=30mm,
    bottom=25mm,
    headheight=25pt,
    headsep=8mm
}

% ===== 图片路径 =====
\graphicspath{{images/}}

% ===== 禁止图表浮动 =====
\usepackage{placeins}
\makeatletter
\def\fps@figure{H}
\def\fps@table{H}
\def\fps@sphinxfigure{H}
\def\fps@sphinxTable{H}
\makeatother

% ==== 强制图片后换行 ===
\usepackage{etoolbox}
\AtEndEnvironment{figure}{\par\noindent}
\AtEndEnvironment{sphinxfigure}{\par\noindent}

% ===== 代码高亮 =====
\usepackage{listings}

% ===== PDF书签 =====
\usepackage{bookmark}

% ===== 自定义变量 =====
\newcommand{\docversion}{''' + release + r'''}
\newcommand{\docname}{''' + project + r'''}

% ===== 页眉页脚 =====
\usepackage{fancyhdr}
\usepackage{lastpage} 

\fancypagestyle{normal}{
    \fancyhf{}  
    \fancyhead[L]{\raisebox{-0.15cm}{\includegraphics[height=0.7cm]{Logo.png}}}
    \fancyhead[R]{\nouppercase{\leftmark}}  
    \fancyfoot[L]{版本 \docversion}
    \fancyfoot[C]{\thepage/\pageref*{LastPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt} 
    \renewcommand{\footrulewidth}{0.4pt}
}

\fancypagestyle{plain}{
    \fancyhf{}
    \fancyhead[L]{\raisebox{-0.15cm}{\includegraphics[height=0.7cm]{Logo.png}}}
    \fancyfoot[L]{版本 \docversion}
    \fancyfoot[C]{\thepage/\pageref*{LastPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0pt}   
    \renewcommand{\footrulewidth}{0.4pt}
}

% ===== 标题样式 =====
\usepackage{titlesec}
\usepackage{xcolor}
\definecolor{TitleRed}{HTML}{D80C1E}

\titlespacing*{\chapter}{0pt}{-30pt}{20pt}
\titleformat{\chapter}{\Huge\bfseries\color{TitleRed}}{\thechapter}{0.5em}{}
\titleformat{\section}{\Large\bfseries\color{TitleRed}}{\thesection}{0.5em}{}
\titleformat{\subsection}{\large\bfseries\color{TitleRed}}{\thesubsection}{0.5em}{}
\titleformat{\subsubsection}{\normalsize\bfseries\color{TitleRed}}{\thesubsubsection}{0.5em}{}

% ===== 超链接颜色 =====
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
    citecolor=blue
}

% ===== 目录颜色控制 =====
\let\origsphinxtableofcontents\sphinxtableofcontents
\renewcommand{\sphinxtableofcontents}{
    \begingroup
    \cleardoublepage
    \pagenumbering{Roman}
    \pagestyle{plain} 
    \hypersetup{linkcolor=black}
    \origsphinxtableofcontents
    \clearpage
    \endgroup
    \pagenumbering{arabic}
    \pagestyle{normal}
}

\let\origlistoffigures\listoffigures
\renewcommand{\listoffigures}{
    \begingroup
    \hypersetup{linkcolor=black}
    \origlistoffigures
    \endgroup
}

\let\origlistoftables\listoftables
\renewcommand{\listoftables}{
    \begingroup
    \hypersetup{linkcolor=black}
    \origlistoftables
    \endgroup
}

% ===== 表格样式修复 (关键修复点) =====
\definecolor{sphinxstyletheadbackground}{rgb}{0.9,0.9,0.9}

\makeatletter
% 修复：使用 \cellcolor 而不是直接放颜色命令
\def\sphinxstyletheadfamily{\small\sffamily\bfseries\color{black}\cellcolor{sphinxstyletheadbackground}}
\makeatother

% ===== 表格跨页与宽度控制 =====
\usepackage{tabularx}
\usepackage{ltablex}
\keepXColumns
\renewcommand{\tabularxcolumn}[1]{m{#1}}
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}

% ===== 代码块分页优化 =====
\sphinxsetup{verbatimwithframe=false}

% ===== 中文图表名称 =====
\AtBeginDocument{
    \renewcommand{\figurename}{图}
    \renewcommand{\tablename}{表}
    \renewcommand{\listfigurename}{图目录}
    \renewcommand{\listtablename}{表目录}
    \setlength{\cftfignumwidth}{3em}
    \setlength{\cfttabnumwidth}{3em}
}
''',
}

latex_additional_files = [
    '_static/cover.tex',
    '_static/backcover.tex',
    '_static/Logo.png',
    '_static/官网二维码.png',
    '_static/Kargo.png',
]

latex_keep_old_macro_names = True
latex_use_xindy = False
latex_toplevel_sectioning = 'chapter'

latex_elements.update({
    'releasename': '版本',
})

# -- todo extension ---------------------------------------
todo_include_todos = True

# -- autodoc ----------------------------------------------
autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

def setup(app):
    app.add_css_file('custom.css')

latex_elements['utf8extra'] = ''