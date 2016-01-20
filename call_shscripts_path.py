import subprocess, sys, shutil

path = sys.argv[1]

# sys.argv[1] = "/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10/runScript_mouse.sh"

print (path)

subprocess.call([path])

# x = sys.argv[1]
# y = "./" + x

# src = "/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/test_runscripts/" + x
# dst = "/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10/"

# shutil.copy(src, dst)

# subprocess.call([y])

# subprocess.call(["/groups/immdiv_bio/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10/runScript_mouse.sh", x])

# subprocess.call(["sh","/groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10", y])
# /groups/immdiv-bioinfo/evergrande/copy_work/yael/FC_01744/Project_yael/mouse_S9-S10: is a directory

#subprocess.call(['./runScript_mouse.sh']) worked!

# print ("works!")