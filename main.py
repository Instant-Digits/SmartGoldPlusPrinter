from firebase import Firebase
from functions import configPrinter
from uuid import getnode as get_mac
from dotMatrixPrinter import setDotMatrixPrinting
from thermalPrinter import setThermalPrinting
from labelPrinter import setLabelPrinting
import requests 
import time

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
while True:
    try:
        requests.get('https://www.google.com/').status_code
        break
    except:
        time.sleep(5)
        print ('Waiting for internet')
        pass


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
        if(data and thermalPrinter):
            #setThermalPrinting(thermalPrinter,metaData,data)            
            try :
                setThermalPrinting(thermalPrinter,metaData,data)                
            except :
                print('printer error')
                thermalPrinter = configPrinter(metaData['config']['thermalPrinter'], 'thermalPrinter', 4)
                if(thermalPrinter):
                    setThermalPrinting(thermalPrinter,metaData,data)
                
            db.child(metaData['firmID']+'/thermalPrint').remove()

        elif not (thermalPrinter):
            thermalPrinter = configPrinter(metaData['config']['thermalPrinter'], 'thermalPrinter', 4)

    db.child(metaData['firmID']+'/thermalPrint').stream(listener)


if ('labelPrinter' in metaData['config']):
    labelPrinter = False
    def listener(message):        
        global labelPrinter
        data=message["data"]       
        if(data and labelPrinter):
            try :
                setLabelPrinting(labelPrinter,metaData,data)                
            except :
                print('printer error')
                labelPrinter = configPrinter(metaData['config']['labelPrinter'], 'labelPrinter', 4)
                if (labelPrinter):
                    setLabelPrinting(labelPrinter,metaData,data)

            db.child(metaData['firmID']+'/labelPrinter').remove()

        elif not (labelPrinter):
            labelPrinter = configPrinter(metaData['config']['labelPrinter'], 'labelPrinter', 4)

    db.child(metaData['firmID']+'/labelPrinter').stream(listener)


if ('formPrinter' in metaData['config']):
    formPrinter = False
    def listener(message):
        global formPrinter
        data=message["data"]        
        if(data and formPrinter):  
            try :
                setDotMatrixPrinting(formPrinter,metaData,data)
                
            except :
                print('printer error')
                formPrinter = configPrinter(metaData['config']['formPrinter'], 'formPrinter', 4)
                if (formPrinter):
                    setDotMatrixPrinting(formPrinter,metaData,data)

            db.child(metaData['firmID']+'/formPrint').remove()

        elif not (formPrinter):
            formPrinter = configPrinter(metaData['config']['formPrinter'], 'formPrinter', 4)
            
    db.child(metaData['firmID']+'/formPrint').stream(listener)

