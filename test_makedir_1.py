# Task1: make a dir
# Task2: Copy a txt file to a dir

import os
import shutil

file_path = "/Users/connie/Desktop/skywalker/"

os.makedirs(file_path);

src = "/Users/connie/Desktop/empty.txt"
dst = "/Users/connie/Desktop/skywalker"

shutil.copy(src, dst);

print ("Good!")