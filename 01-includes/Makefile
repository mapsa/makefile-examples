# Use of Makefiles including a configuration file
#
.EXPORT_ALL_VARIABLES:
BUILD ?= glasgow

OUTPUTDIR = $(HOME)/sdf/smeresults/latepayments/$(BUILD)

PARAMS := config/$(BUILD).mk
include $(PARAMS)

all: xtabs

xtabs: xtabs.py
	@echo Running xtabs
	@echo Output dir: $(OUTPUTDIR)
	@echo $(BUILD) postal districts: $(postal_districts)
	@python xtabs.py 

