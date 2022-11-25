.PHONY: all test validate sim doc pdf html clean variables help
###############################################################################
# Makefiles documentation
#
# The target help will print the text after "##" for each target
#
###############################################################################

OUTPUTDIR = $(CURDIR)/output

all: ## run all. This is the default target (because it's the first one) 

test: ## Perform self test cases 

validate: ## Compare outputs from 2 versions of the code

sim: ## Run a simulation

doc: ## Creates code documentation

pdf: ## Creates a pdf file

html: ## Creates html files

clean: ## Delete all output files or folder created by this makefile

variables: ## Print variables
	@echo OUTPUTDIR=$(OUTPUTDIR)
help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |\
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m\
	%s\n", $$1, $$2}'
