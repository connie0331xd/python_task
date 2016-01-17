import os, sys

filespath_test =  "LIB017913_TRA00045276_S1_L001_R1.fastq.bz2"

cmdstring = "bzip2 -d %s" % (filespath_test)
os.system(cmdstring)
