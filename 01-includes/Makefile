# Use of Makefiles including a configuration file
#

BUILD ?= glasgow

OUTPUTDIR = $(HOME)/sdf/smeresults/latepayments/$(BUILD)

PARAMS := config/$(BUILD).mk
include $(PARAMS)

all: xtabs

xtabs: 
	@echo Running xtabs
	@echo Output dir: $(OUTPUTDIR)
	@echo $(BUILD) postal districts: $(postal_districts)

