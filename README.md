This repository contains data files & scripts for producing fillable PDF
checklists of the DIY recipes available in *Animal Crossing: New Horizons*.
The actual resulting PDFs can be downloaded from [the "Releases"
page](https://github.com/jwodder/acnh-diy-checklist/releases).


Running the `mkchecklist.py` Script
===================================

Needed:

- Python 3.6+
- the Python packages listed in `requirements.txt`
- the data files in `data/` or compatible CSV files

Run the script as:

```
python3 mkchecklist.py [--by <field>] [--checked <file>] path/to/recipes.csv path/to/seasons.csv
```

This will output the source for a LaTeX document that will produce a fillable
PDF when typeset.

- The `--by` option can be set to `name`, `source`, or `category` to set how
  the checklist will be organized (default: `name`).

- The `--checked` option can be supplied with the path to a file listing the
  names of DIY recipes, one per line, in order to produce a PDF in which those
  recipes start out checked-off.
