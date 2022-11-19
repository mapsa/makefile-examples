# This example create targets from a function
# The method call is used to create the rule

PYTHON = @python3
N = 1 2 3

SRCS = $(addsuffix .py, $(addprefix script,$(N)))
OBJS = $(addsuffix .txt, $(addprefix output,$(N)))

define run-python-script
output$(1).txt: script$(1).py
	$(PYTHON) $$< $$@
endef

all: $(OBJS)

$(foreach n,$(N),\
	$(eval $(call run-python-script,$(n))) \
)

clean:
	rm $(OBJS)

