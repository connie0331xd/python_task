import subprocess, sys

x = sys.argv[1]
y = "./" + x

subprocess.call([y])

# subprocess.call(["sh","/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10", y])
# /groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10: is a directory

#subprocess.call(['./runScript_mouse.sh']) worked!

# print ("works!")