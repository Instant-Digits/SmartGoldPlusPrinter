import os
try :
    from firebase import Firebase
except :
    os.system('sudo pip3 install pyrebase firebase')
    from firebase import Firebase
    print('Firebase Installed Again')

from uuid import getnode as get_mac
import requests 
import time
from functions import configPrinter
from dotMatrixPrinter import setDotMatrixPrinting
from thermalPrinter import setThermalPrinting
from labelPrinter import setLabelPrinting
from InvoicePrinter import setPDFInvoicePrinter
from wifiCheck import waitForInternet


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

waitForInternet(4)


mac = get_mac()
print ('Mac : '+str(mac))
metaData=db.child('/Printers/'+str(mac)).get().val();
try :
        metaData= dict(metaData)
except TypeError:
        print ('Invalued config')



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


if ('labelPrinterr' in metaData['config']):
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


if  ('invoicePrinter' in metaData['config']):
    formPrinter = False
    def listener(message):
        global formPrinter
        data=message["data"] 
        # if not (formPrinter):
        #     formPrinter = configPrinter(metaData['config']['formPrinter'], 'formPrinter', 1)       
        if(data):  
            try :
                setPDFInvoicePrinter('invoicePrinter','metaData',data)
                
            except :
                print('printer error')
                # formPrinter = configPrinter(metaData['config']['formPrinter'], 'formPrinter', 1)
                # if (formPrinter):
                #     setDotMatrixPrinting(formPrinter,metaData,data)

            #db.child(metaData['firmID']+'/formPrint').remove()

            
    db.child(metaData['firmID']+'/invoicePrint').stream(listener)

