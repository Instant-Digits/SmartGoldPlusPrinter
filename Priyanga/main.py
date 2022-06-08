import os
import time
time.sleep(1)
from wifiCheck import waitForInternet

try :
    from firebase import Firebase
except :
    waitForInternet(4)
    os.system('sudo pip3 install pyrebase==3.0.3 firebase==3.0.1')
    from firebase import Firebase
    print('Firebase Installed Again')

from functions import configPrinter
from uuid import getnode as get_mac
from dotMatrixPrinter import setDotMatrixPrinting
from thermalPrinter import setThermalPrinting
from labelPrinter import setLabelPrinting
from certificatePrinter import SetPrintingJobCertificate


config = {
        "apiKey": "AIzaSyAHiNXjCfRz_aQefCYoFglXo4ramCMcyIE",
        "authDomain":  "smart-pos-plus-secondary.firebaseapp.com",
        "databaseURL":  "https://smart-pos-plus-secondary-default-rtdb.firebaseio.com",
        "storageBucket": "smart-pos-plus-secondary.appspot.com"
    }
firebasecon = Firebase(config)
db = firebasecon.database()

printers={}

print ('System start')

mac = get_mac()
print ('Mac : '+str(mac))
waitForInternet(4)


metaData=db.child('/Printers/'+str(mac)).get().val();
try :
        metaData= dict(metaData)
except TypeError:
        print ('Invalued config')

print(metaData["config"])



if ('thermalPrinter' in metaData['config']):
    thermalPrinter = False
    def listener(message):
        global thermalPrinter
        data=message["data"]
        if not (thermalPrinter):
            thermalPrinter = configPrinter(metaData['config']['thermalPrinter'], 'thermalPrinter', 1)        
        if(data and thermalPrinter):
            #setThermalPrinting(thermalPrinter,metaData,data)            
            try :
                setThermalPrinting(thermalPrinter,metaData,data)                
            except :
                print('printer error')
                thermalPrinter = configPrinter(metaData['config']['thermalPrinter'], 'thermalPrinter', 1)
                if(thermalPrinter):
                    setThermalPrinting(thermalPrinter,metaData,data)
                
            db.child(metaData['firmID']+'/thermalPrint').remove()
        

    db.child(metaData['firmID']+'/thermalPrint').stream(listener)


if ('labelPrinter' in metaData['config']):
    labelPrinter = False
    def listener(message):        
        global labelPrinter
        data=message["data"]
        if not (labelPrinter):
            labelPrinter = configPrinter(metaData['config']['labelPrinter'], 'labelPrinter', 1)       
        if(data and labelPrinter):
            try :
                setLabelPrinting(labelPrinter,metaData,data)                
            except :
                print('printer error')
                labelPrinter = configPrinter(metaData['config']['labelPrinter'], 'labelPrinter', 1)
                if (labelPrinter):
                    setLabelPrinting(labelPrinter,metaData,data)

            db.child(metaData['firmID']+'/labelPrinter').remove()

        
    db.child(metaData['firmID']+'/labelPrinter').stream(listener)


if ('formPrinter' in metaData['config']):
    formPrinter = False
    def listener(message):
        global formPrinter
        data=message["data"]   
        if not (formPrinter):
            formPrinter = configPrinter(metaData['config']['formPrinter'], 'formPrinter', 1)     
        if(data and formPrinter):  
            try :
                setDotMatrixPrinting(formPrinter,metaData,data)
                
            except :
                print('printer error')
                formPrinter = configPrinter(metaData['config']['formPrinter'], 'formPrinter', 1)
                if (formPrinter):
                    setDotMatrixPrinting(formPrinter,metaData,data)

            db.child(metaData['firmID']+'/formPrint').remove()

            
    db.child(metaData['firmID']+'/formPrint').stream(listener)



if ('certificatePrinter' in metaData['config']):
    def listener(message):
        data=message["data"]        
        if(data):  
            #setDotMatrixPrinting(printers['formPrinter'],metaData,data)          
            try :
                SetPrintingJobCertificate(data)
                db.child(metaData['firmID']+'/certificatePrinter').remove()
            except :
                print('printer error')
                SetPrintingJobCertificate(data)
            
    db.child(metaData['firmID']+'/certificatePrinter').stream(listener)

