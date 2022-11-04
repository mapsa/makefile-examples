QMDFILE = main.qmd
PDFFILE = $(TEXFILES:.qmd=.pdf)
PPTXFILE = $(TEXFILES:.qmd=.pptx)

all: beamer pptx

install:
	@quarto install tool tinytex

beamer: $(QMDFILE)
	@quarto render $< --to beamer 

pptx: $(QMDFILE)
	@quarto render $< --to pptx 

clean:
	@rm -f $(PDFFILE) $(PPTXFILE)

.PHONY: beamer pptx clean install all

