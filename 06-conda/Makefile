.EXPORT_ALL_VARIABLES:
.ONESHELL:
.PHONY: all install

# Conda settings
CONDAROOT = $$(conda info --base)
CONDA_ACTIVATE = source $(CONDAROOT)/etc/profile.d/conda.sh ; conda activate ; conda activate
ENV = ./env

all: test.py $(ENV)
	$(CONDA_ACTIVATE) $(ENV); \
	python $<

$(ENV): environment.yml
	conda env update --prefix $(ENV) --file $< --prune

clean:
	rm -rf $(ENV)

