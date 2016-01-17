# Task: look in a dir -> assign all of the files in the dir to an array ->
# loop through that array -> print out the elements of the array

import os

all_files = []

for root, dirs, files in os.walk("/home/yj88/test_li/"):
    all_files.extend(files)
    print(files)
    for f in files:
        os.path.join(root, f)