PYTHON ?= python3

all : recipes-byname.pdf recipes-bysource.pdf recipes-bycategory.pdf

%.pdf : %.tex
	latexmk -pdf $<

recipes-byname.tex : mkchecklist.py data/recipes.csv data/seasons.csv
	$(PYTHON) mkchecklist.py data/recipes.csv data/seasons.csv > $@

recipes-bysource.tex : mkchecklist.py data/recipes.csv data/seasons.csv
	$(PYTHON) mkchecklist.py --by source data/recipes.csv data/seasons.csv > $@

recipes-bycategory.tex : mkchecklist.py data/recipes.csv data/seasons.csv
	$(PYTHON) mkchecklist.py --by category data/recipes.csv data/seasons.csv > $@

open : all
	open *.pdf

clean :
	latexmk -c
	rm -f *.tex

distclean :
	latexmk -C
	rm -f *.tex
