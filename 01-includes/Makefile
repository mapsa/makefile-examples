# Use of Makefiles including a configuration file
#
# The primary targets in this file are
# 
# all		Run the pipeline for the entire dataset
# glasgow 	Restrict the results only for some postal districts
# 		in the Glasgow City Region
#

BUILD ?= glasgow

OUTPUTDIR = $(HOME)/sdf/smeresults/latepayments/$(BUILD)

PARAMS := config/$(BUILD).mk
include $(PARAMS)

MIRO = miro -f -q

all: xtabs

xtabs: 
	@echo Running xtabs
	@echo Output dir: $(OUTPUTDIR)
	@echo $(BUILD) postal districts: $(postal_districts)

