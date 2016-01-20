import subprocess, sys, glob, os, shutil

x = sys.argv[1]

folder = "/home/yj88/test_li/"

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
