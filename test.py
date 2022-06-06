import time 
import os

lastCheckTime = time.time()

#lprm -





while (True):
    if(time.time()>lastCheckTime+3):
        lastCheckTime = time.time()
        os.system('lpstat -t')
        print ('Printer Refresh')
