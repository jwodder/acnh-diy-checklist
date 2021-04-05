all : recipes-byname.pdf

recipes-byname.pdf : recipes-byname.tex
	latexmk -pdf recipes-byname.tex

recipes-byname.tex : make-byname.py data/recipes.csv data/seasons.csv
	python3 make-byname.py data/recipes.csv data/seasons.csv > $@

open : all
	open *.pdf

clean :
	latexmk -c
	rm -f *.tex

distclean :
	latexmk -C
	rm -f *.tex
