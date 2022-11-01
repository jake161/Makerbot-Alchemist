import os 
import time

time.sleep(1)
# define path for file
GCODE=os.getcwd() + "\\input.gcode"
GPX=os.getcwd() + "\\gpx.exe"
NAMER=os.getcwd() + "\\namer.py"
while 1:
    if os.path.exists(GCODE):

        os.system(GPX + ' -g '+ GCODE)
        
        os.system('python ' + NAMER)
        break
    else:
        print("\nError no input file\n") 
        break