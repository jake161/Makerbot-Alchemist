import os 
import subprocess

# define path for file
PPS = os.getcwd()+"\\PPS.py"

while 1:
    if os.path.exists(PPS):
        subprocess.Popen('python '+ PPS)
        print("Triggering!\n")
		
        break
    else:
        print("Error, source files missing\n")
        break
