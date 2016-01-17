import os, sys

all_files = []

folder = "/Users/connie/Desktop/test_file/"

for root, dirs, files in os.walk(folder):
    all_files.extend(files)
    
    cmdstring = "bzip2 -d %s" % (flies)
    os.system(cmdstring)

#filespath_test =  "LIB017913_TRA00045276_S1_L001_R1.fastq.bz2"