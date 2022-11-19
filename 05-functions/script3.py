import sys

args = sys.argv
filename = args[1]
f = open(filename, "a")
f.write("Script 3 done!")
f.close()

