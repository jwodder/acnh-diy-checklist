from   collections import namedtuple
import csv
from   operator    import attrgetter
import click

class Recipe(namedtuple("Recipe", "name source_group source notes")):
    @property
    def name_key(self):
        return self.name.lower()

    def check_item(self):
        if self.source_group == "Balloons":
            fmt = r"\checkitem{{{name}}} — Balloons ({source})"
        else:
            fmt = r"\checkitem{{{name}}} — {source}"
        if self.notes:
            fmt += " ({notes})"
        return fmt.format_map(self._asdict())


HEAD = r"""\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[hmargin=0.75in,vmargin=1in]{geometry}
\usepackage{booktabs}
\usepackage{caption}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage{lastpage}
\usepackage{multicol}
\usepackage{xcolor}

\pagestyle{fancy}
\fancyhead[L]{\emph{Animal Crossing: New Horizons} DIY Recipes}
\fancyhead[C]{}
\fancyhead[R]{[\thepage/\pageref{LastPage}]}
\fancyfoot[L]{\footnotesize <\url{https://www.github.com/jwodder/acnh-diy-checklist}>}
\fancyfoot[C]{}
\renewcommand{\footrulewidth}{\headrulewidth}

\newcommand{\checkitem}[1]{\CheckBox[width=5pt,height=5pt,bordercolor=black]{#1}}

\usepackage[hidelinks]{hyperref}
\def\LayoutCheckField#1#2{\item[#2] #1}
\begin{document}
"""

@click.command()
@click.argument("recipes_file", type=click.File())
@click.argument("seasons_file", type=click.File())
def main(recipes_file, seasons_file):
    with recipes_file:
        recipes = [Recipe(**row) for row in csv.DictReader(recipes_file)]
    with seasons_file:
        seasons = list(csv.DictReader(seasons_file))
    print(HEAD)
    show_seasons(seasons)
    print(r"\begin{Form}")
    print(r"\begin{multicols}{2}")
    print(r"\small")
    print(r"\begin{itemize}[noitemsep]")
    recipes.sort(key=attrgetter("name_key"))
    for r in recipes:
        print(r.check_item())
    print(r"\end{itemize}")
    print(r"\end{multicols}")
    print(r"\end{Form}")
    print(r"\end{document}")

def show_seasons(seasons):
    print(r"\begin{table}")
    print(r"\begin{center}")
    print(r"\caption*{\textbf{Balloon Seasons}}")
    print(r"\begin{tabular}{ll@{\enskip--\enskip}ll@{\enskip--\enskip}l}")
    print(r"\toprule")
    print(
        r"\textbf{Season} & \multicolumn{2}{l}{\textbf{Northern Hemisphere}} &"
        r" \multicolumn{2}{l}{\textbf{Southern Hemisphere}} \\"
    )
    print(r"\midrule")
    for s in seasons:
        print(
            r"{name} & {northern_start} & {northern_end} & {southern_start} &"
            r" {southern_end} \\".format_map(s)
        )
    print(r"\bottomrule")
    print(r"\end{tabular}")
    print(r"\end{center}")
    print(r"\end{table}")

if __name__ == "__main__":
    main()
