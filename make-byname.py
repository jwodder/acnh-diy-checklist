import csv
import re
import sys

recipes_file, seasons_file = sys.argv[1:]

print(r"\documentclass[10pt]{article}")
print(r"\usepackage[T1]{fontenc}")
print(r"\usepackage[utf8]{inputenc}")
print(r"\usepackage[hmargin=0.75in,vmargin=1in]{geometry}")
print(r"\usepackage{booktabs}")
print(r"\usepackage{caption}")
print(r"\usepackage{fancyhdr}")
print(r"\usepackage{enumitem}")
print(r"\usepackage{lastpage}")
print(r"\usepackage{multicol}")
print(r"\usepackage{xcolor}")

print(r"\pagestyle{fancy}")
print(r"\fancyhead[L]{\emph{Animal Crossing: New Horizons} DIY Recipes}")
print(r"\fancyhead[C]{}")
print(r"\fancyhead[R]{[\thepage/\pageref{LastPage}]}")
print(r"\fancyfoot[L]{\footnotesize <\url{https://www.github.com/jwodder/acnh-diy-checklist}>}")
print(r"\fancyfoot[C]{}")
print(r"\renewcommand{\footrulewidth}{\headrulewidth}")

print(r"\newcommand{\checkitem}[1]{\CheckBox[width=5pt,height=5pt,bordercolor=black]{#1}}")

print(r"\usepackage[hidelinks]{hyperref}")
print(r"\def\LayoutCheckField#1#2{\item[#2] #1}")
print(r"\begin{document}")

print(r"\begin{table}")
print(r"\begin{center}")
print(r"\caption*{\textbf{Balloon Seasons}}")
print(r"\begin{tabular}{ll@{\enskip--\enskip}ll@{\enskip--\enskip}l}")
print(r"\toprule")
print(r"\textbf{Season} & \multicolumn{2}{l}{\textbf{Northern Hemisphere}} & \multicolumn{2}{l}{\textbf{Southern Hemisphere}} \\")
print(r"\midrule")
with open(seasons_file) as fp:
    for row in csv.DictReader(fp):
        print(r"{name} & {northern_start} & {northern_end} & {southern_start} & {southern_end} \\".format_map(row))
print(r"\bottomrule")
print(r"\end{tabular}")
print(r"\end{center}")
print(r"\end{table}")

print(r"\begin{Form}")
print(r"\begin{multicols}{2}")
print(r"\small")
print(r"\begin{itemize}[noitemsep]")

with open(recipes_file) as fp:
    inp = csv.DictReader(fp)
    for row in sorted(inp, key=lambda r: r["name"].lower()):
        if row["source_group"] == "Balloons":
            item = "\checkitem{{{name}}} — Balloons ({source})"
        else:
            item = "\checkitem{{{name}}} — {source}"
        if row["notes"]:
            item += " ({notes})"
        print(item.format_map(row))

print(r"\end{itemize}")
print(r"\end{multicols}")
print(r"\end{Form}")

print(r"\end{document}")
