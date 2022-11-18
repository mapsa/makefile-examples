# Makefile Essentials for Data Science Projects

A set of notes and Makefiles examples.

# Table of Contents
1. [Uses](#uses)
1. [Basic Concepts](#basic-concepts)
1. [Special Targets](#special-targets)
1. [Automatic Variables](#automatic-variables)
1. [Execution](#execution)
1. [Debugging](#debugging)
1. [References](#references)

## Uses

1. **Reproducible Research**
1. **Task Dependency Management**
1. **Pipeline Documentation**

## Basic Concepts

Make is a build automation tool to build targets based on recipes:

1. **Targets:** what to build (a file or a phony target)
1. **Rules:** how to build the target
1. **Prerequisites (optional):** dependencies

```bash
target: prerequisite1 prerequisite2 prerequisite3 prerequisite5
<tab>   command_A
<tab>   command_B

prerequisite1: prerequisite4
<tab>   command_C

prerequisite2: prerequisite4
<tab>   command_D

prerequisite4:
<tab>   command_E
```

<img src="img/makefile.png" alt="drawing" width="400"/>

To perform a build, make will construct a direct acyclic graph (DAG) from the rules.

By default, when you type `make` it will try to find a Makefile with the following names, in order: **GNUmakefile**, **makefile** and **Makefile** (the most common one). 

You can also call it differently but you need to run it as `make -f mymakefile`.

## [Special Targets](https://www.gnu.org/software/make/manual/html_node/Special-Targets.html)

**.PHONY**

The prerequisites of the special target .PHONY are considered to be phony targets. When it is time to consider such a target, make will run its recipe unconditionally, regardless of whether a file with that name exists or what its last-modification time is. 

```bash
.PHONY: all target1 target2 target3 clean

OUTDIR = output

all: target1 target2 

target1: prerequisite1
<tab>   command_A

target2: prerequisite1
<tab>   command_B

clean:
<tab>   rm -rf $(OUTDIR)
```

**.EXPORT_ALL_VARIABLES**

Simply by being mentioned as a target, this tells make to export all variables to child processes by default.

**.DELETE_ON_ERROR**

Delete the target of a rule if it has changed and its recipe exits with a nonzero exit status.

**.ONESHELL**

 When a target is built all lines of the recipe will be given to a single invocation of the shell.

## [Automatic Variables](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html)

### **$@**

The file name of the target of the rule. 

```bash
target1: prerequisite1
<tab>   echo $@
```
Will print `target1`.

### **$<**

The name of the first prerequisite.

```bash
target1: prerequisite1 prerequisite2
<tab>   echo $<
```
Will print `prerequisite1`.


### **$\***

The stem with which an **implicit rule** matches.

```bash
$(OUTDIR)/my_%_file.csv: prerequisite1 
<tab>   echo $*
```
If in the folder OUTDIR you have a csv file called `my_first_file.csv`, this will print `first`.


## [Execution](https://www.gnu.org/software/make/manual/html_node/Options-Summary.html)

**Parallel Execution**

You can use `-j` to run in parallel (limited to number of CPUs and RAM available) or specify the number of parallel processes `N`. 
```bash
make -j
make -j N
```

**Rebuild a Target**

Forces make to ignore existing targets

```bash
make target1 -B
```

**Keep Going**

Continue as much as possible after an error. 

```bash
make target1 -k
```

## Debugging

## Visualization


## References

- https://www.gnu.org/software/make/manual/html_node/index.html

