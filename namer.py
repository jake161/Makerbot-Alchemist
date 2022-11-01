import os 
import time

time.sleep(1)
# define path for file
X3G = os.getcwd() + "\\input.x3g"
GCODE = os.getcwd() + "\\input.gcode"

while 1:
    if os.path.exists(X3G):
        
        name=(input("\nPlease name the file\n"))
        #print(name)
        #time.sleep(5)
        
        old_file = (X3G)
        new_file = (os.getcwd() + "\\" + name + ".x3g")
        os.rename(old_file,new_file)
        
        old_file2 = (GCODE)
        new_file2 = (os.getcwd() + "\\" + name + ".gcode")
        os.rename(old_file2,new_file2)
        break
    else:
        print("Error, x3g not found\n")
        break