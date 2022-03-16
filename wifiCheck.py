import os
import time
import urllib.request
import os

def waitForInternet(timeOut=5): #min
    timeStart = time.time()
    timeOut=timeOut*60
    while(True):
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            print ("internet connected")
            return True
        except:
            print ("waiting for internet")
            time.sleep(5)
            if (time.time()>timeStart+timeOut and os.uname()[1]=='raspberrypi'):
                print ("waiting timeout for internet")
                wifiReset()
                return False


def wifiReset():
    print('wifi reset started')
    os.system('sudo wifi-connect -s "Wifi Setup"')
    waitForInternet(1)
    #os.system('sudo reboot')
    return