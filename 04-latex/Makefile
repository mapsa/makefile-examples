.ONESHELL:
TEXFILES = main.tex
PDFFILES = $(TEXFILES:.tex=.pdf)

all: pdf


pdf: $(TEXFILES)
	@pdflatex $(TEXFILES:.tex=)
	@bibtex $(TEXFILES:.tex=)
	@pdflatex $(TEXFILES:.tex=)
	@pdflatex $(TEXFILES:.tex=)
	@rm $(TEXFILES:.tex=).{aux,log,bbl,blg}

clean:
	@rm -f $(TEXFILES:.tex=).{aux,out,bbl,bcf,blg,idx,log,toc,run.xml,synctex.gz}

open:
	@open $(PDFFILES) &> /dev/null &

.PHONY: pdf clean all

