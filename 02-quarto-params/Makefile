SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.ONESHELL:
.DELETE_ON_ERROR:

X = 10 20 30 40 50
HTMLS = $(addsuffix .html, $(addprefix test_, $(X)))

all: $(HTMLS)

test_%.html: test.qmd
	quarto render test.qmd -P x:$* --output $@
