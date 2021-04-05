all : recipes-byname.pdf recipes-bysource.pdf recipes-bycategory.pdf

recipes-byname.pdf : recipes-byname.tex
	latexmk -pdf recipes-byname.tex

recipes-byname.tex : mkchecklist.py data/recipes.csv data/seasons.csv
	python3 mkchecklist.py data/recipes.csv data/seasons.csv > $@

recipes-bysource.pdf : recipes-bysource.tex
	latexmk -pdf recipes-bysource.tex

recipes-bysource.tex : mkchecklist.py data/recipes.csv data/seasons.csv
	python3 mkchecklist.py --by source data/recipes.csv data/seasons.csv > $@

recipes-bycategory.pdf : recipes-bycategory.tex
	latexmk -pdf recipes-bycategory.tex

recipes-bycategory.tex : mkchecklist.py data/recipes.csv data/seasons.csv
	python3 mkchecklist.py --by category data/recipes.csv data/seasons.csv > $@

open : all
	open *.pdf

clean :
	latexmk -c
	rm -f *.tex

distclean :
	latexmk -C
	rm -f *.tex
