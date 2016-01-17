filepath =  "LIB017913_TRA00045276_S1_L001_R1.fastq.bz2" # Creat a new path of the filename
newfilepath = filepath[:-11] # read until R, then stop.

newpath = "/home/yj88/test_li/"+newfilepath # the path of new folder

#Create a folder with os.makedirs() and use os.path.exists() to see if it already exists
if not os.path.exists(newpath): 
    os.makedirs(newpath)

bz2_1 = bz2.BZ2File("LIB017913_TRA00045276_S1_L001_R1.fastq.bz2")
bz2_1.bz2.decompress(newpath)
bz2_1.close()

bz2_2 = bz2.BZ2File("LIB017913_TRA00045276_S1_L001_R2.fastq.bz2")
bz2_2.bz2.decompress(newpath)
bz2_2.close()