# Makefile to convert all .md files to PDFs

MD_FILES := $(wildcard *.md)
PDF_FILES := $(MD_FILES:.md=.pdf)
TEMPLATEDIR = pandoc-latex-template

all: $(PDF_FILES)

%.pdf: %.md Makefile
	pandoc $< -o $@ --template $(TEMPLATEDIR)/eisvogel.tex --resource-path=$(TEMPLATEDIR)

clean:
	rm -f $(PDF_FILES)

.PHONY: all clean

# Notes:  clone https://github.com/Wandmalfarbe/pandoc-latex-template.git
# as a submodule, and ensure you have Texlive and fonts installed:
# apt install texlive texlive-fonts-extra
