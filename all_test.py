import glob, os, shutil, subprocess, sys

x = sys.argv[1]

subprocess.call(["bz2","/home/yj88/test_li/", sys.argv[1]])

print ("First step!")

all_files = []

folder = "/home/yj88/test_li/"

for root, dirs, files in os.walk(folder):
    all_files.extend(files)
    print (files)

    for name in files:
        cmdstring = "bzip2 -d %s" % (name)
        os.system(cmdstring)

#print ("Good!")
        
for file_path in glob.glob(os.path.join(folder, '*.*')):
    new_dir = file_path.rsplit('.', 1)[0]
    try:
        os.mkdir(os.path.join(folder, new_dir))
    except WindowsError:
        # Handle the case where the target dir already exist.
        pass
    shutil.copy(file_path, os.path.join(new_dir, os.path.basename(file_path)))
    
#print ("Excellent!")