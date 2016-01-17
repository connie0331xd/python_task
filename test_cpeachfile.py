# Task1: make 5 folders which the folder name is a file name 
# Task2: copy each file to correct folder

import os, shutil

myfolders = [] #Create a list(=an array) 

src = "/Users/connie/Desktop/empty/"

final_path = "/Users/connie/Desktop/" #/Users/connie/Desktop/empty does not work
# error: FileExistsError: [Errno 17] File exists: '/Users/connie/Desktop/empty/empty1.txt'

#其中第一個 dirPath 是這行啟始路徑，
#第二個 dirNames 是一個 list，裡面包含了 dirPath 下所有的資料夾名稱，
#而第三個 fileNames 也是一個 list，包含了 dirPath 下所有的檔案名稱。
#所以我們利用 for 走過 os.walk() 所有的 dirPath，


for dirpath, dirnames, filenames in os.walk(src):
    myfolders.extend(filenames) #如果不是ends with "txt" 的filenames的話 dir就是file.split(".")
    for f in filenames: # 利用 for 走過 os.walk() 所有的 dirPath
        if f.endswith('.txt'):
            Dir = f.split(".")
            # Do not use "dir", pythno will confused: <built-in function dir>
            # .split: http://pydoing.blogspot.tw/2011/03/python-strsplit.html
            # 在{}裡面創造的代號  在{}之後去使用的話  這個代號就會不存在
            # 所以name not defined這個問題就在於  你在if裡面去創造Dir這個variable
            # 但是你在if以外去呼叫Dir這個variable 那就不存在了
            #newDir = os.path.join(final_path, dir)
            #if (not os.path.exists(os.path.join(newdir))):
                #os.makedirs(os.path.join(newdir))
                
            #shutil.copy(os.path.join(dirpath, filenames), newdir)
        
        
#src = "/Users/connie/Desktop/empty/"
#dst = "/Users/connie/Desktop/"

#shutil.copy(src, dst);
        
print(Dir)