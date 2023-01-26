%% Identification part:

\NeedsTeXFormat{LaTeX2e}[1995/12/01]  % Any version, really!
\ProvidesClass{uiomaster}[2022/11/25 v1.0.1 UiO document class for
  master's thesis]

%% Required packages:
\RequirePackage[T1]{fontenc}
\RequirePackage{xifthen}

%% Option declaration part:
\DeclareOption{bachelor}{\def \uiom@base {article}}
\DeclareOption{binding}{\def \uiom@bind {24pt}}
\DeclareOption{font=cmr}{\def \uiom@font {\RequirePackage{lmodern}
    \RequirePackage[scaled]{helvet}}}
\DeclareOption{font=garamond}{\def \uiom@font {\RequirePackage[garamond]{mathdesign}
    \RequirePackage[scaled]{helvet}}}
\DeclareOption{font=times}{\RequirePackage{txfonts}}
\DeclareOption{master}{\def \uiom@base {report}}

\def \uiom@bind {0pt}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{\uiom@base}}

\ExecuteOptions{font=cmr, master}
\ProcessOptions \relax

%% Base class load part:
\ifthenelse{\equal{\uiom@base}{report}}
  {\LoadClass[a4paper,11pt,twoside,openright]{report}}
  {\LoadClass[a4paper,11pt]{article}}

%% Margins:
\RequirePackage[vmargin=3cm,bindingoffset=\uiom@bind]{geometry}

%% Text adjustments:
\pretolerance = 3000
\tolerance = 6000   \hbadness = \tolerance
\setlength{\parskip}{0cm plus 1mm}

%% Select a font
\uiom@font

%% Chapter and section headers:
\RequirePackage[]{titlesec}
\titleformat{\part}[display]
  {\centering\sf\Huge}{\partname\ \thepart}{15pt}{\Huge\sf\bfseries}
\titleformat{\chapter}[display]
  {\sf\huge}{\chaptertitlename\ \thechapter}{15pt}{\Huge\sf\bfseries}
\titleformat{\section}
  {\sf\Large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}
  {\sf\large\bfseries}{\thesubsection}{1em}{}
\titleformat{\subsubsection}
  {\sf\normalsize\bfseries}{\thesubsubsection}{1em}{}
\titleformat{\paragraph}[runin]
  {\sf\normalsize\bfseries}{\theparagraph}{1em}{}
\titleformat{\subparagraph}[runin]
  {\sf\normalsize\bfseries}{\thesubparagraph}{1em}{}
\titlespacing*{\chapter} {0pt}{50pt}{40pt}
\titlespacing*{\section} {0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}
\titlespacing*{\subsection} {0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\titlespacing*{\subsubsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\titlespacing*{\paragraph} {0pt}{3.25ex plus 1ex minus .2ex}{1em}
\titlespacing*{\subparagraph} {\parindent}{3.25ex plus 1ex minus .2ex}{1em}

%% Redefine \begin{abstract}...\end{abstract}
\renewenvironment{abstract}{%
  \ifthenelse{\equal{\uiom@base}{report}}
    {\cleardoublepage
     \markboth{\abstractname}{}%           
     \vspace*{5\baselineskip}}%
    {\bigskip}%
  \small
  \begin{center}%
    {\sf\bfseries \abstractname\vspace{-.5em}\vspace{\z@}}%
  \end{center}%
  \quotation}%
{\endquotation \bigskip}

%% Define \begin{preface}
\newenvironment{preface}{%
  \ifthenelse{\equal{\uiom@base}{report}}
    {\chapter*{\prefacename}
      \markboth{\prefacename}{}}
    {\section*{\prefacename}}}
  {}

%% Headers and footers:
\ifthenelse{\equal{\uiom@base}{report}}
  {\RequirePackage{fancyhdr}
   \fancyhead{}
   \setlength{\headheight}{15pt}
   \fancyhead[LE]{\textsf{\small \nouppercase{\leftmark}}}
   \fancyhead[RO]{\textsf{\small \nouppercase{\rightmark}}}
   \renewcommand{\headrulewidth}{0pt}
   \fancyfoot{}
   \fancyfoot[LE,RO]{\textsf{\thepage}}
   \renewcommand{\footrulewidth}{0pt}
   \pagestyle{fancy}
   \fancypagestyle{plain}{\fancyhead{}}}
 {}

%% Figurer og tabeller
\RequirePackage[labelfont=sf,font=small]{caption}

%% Document parts:
\newcommand{\frontmatter}{\cleardoublepage \pagenumbering{roman}}
\newcommand{\mainmatter}{\cleardoublepage \pagenumbering{arabic}}
\newcommand{\backmatter}{\cleardoublepage}

\providecommand{\preface}{\chapter*{}\markboth{}{}}
\providecommand{\endpreface}{}

\endinput
