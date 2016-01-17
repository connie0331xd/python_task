
import subprocess, sys
#x = argv[1]
#subprocess.call(["php","test_script.php","x"])

x = sys.argv[1]

subprocess.call(["php","/Users/connie/Desktop/test_script.php", sys.argv[1]])
 
# x不能用double quote包住阿
# double quote包住的東西都是string, 沒包的話就是variable
# 你都assign value給x, 所以x是個variable喔!!