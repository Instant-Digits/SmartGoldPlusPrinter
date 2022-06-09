import os
from wifiCheck import waitForInternet
try :
    from firebase import Firebase
except :
    waitForInternet(4)
    os.system('sudo pip3 install pyrebase firebase')
    from firebase import Firebase
    print('Firebase Installed Again')

from certificatePrinter import SetPrintingJobCertificate

from reportPrinter import SetPrintingJobReport
from stockPrinter import SetPrintingJobStock
from uuid import getnode as get_mac
import requests 
import time
from functions import configPrinter
from dotMatrixPrinter import setDotMatrixPrinting
from thermalPrinter import setThermalPrinting
from labelPrinter import setLabelPrinting
from InvoicePrinter import setPDFInvoicePrinter
from cashflowPrinter import setStatementPrinter
from detailsBookPrinter import setDetailBooktPrinter

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
os.system('lprm -')
print ('Pending Printing jobs are cleaned')

waitForInternet(4)


mac = get_mac()
print ('Mac : '+str(mac))
metaData=db.child('/Printers/'+str(mac)).get().val();
try :
        metaData= dict(metaData)
except TypeError:
        print ('Invalued config')


firmIds =metaData['firmID'].split('@')

lastCheckTime = time.time() #printer refresh

def mainListener(message):  
    global lastCheckTime   

    if not (message['data']) :
        return 


    if  ('invoicePrinter' in metaData['config'] and (message['path']=='/invoicePrint' or 'invoicePrint' in message["data"])): #or 'invoicePrint' in message["data"] 
        data=message["data"]  if message['path']=='/invoicePrint' else message["data"]['invoicePrint']
        if(data):  
            try :
                setPDFInvoicePrinter(data)
                lastCheckTime = time.time() #printer refresh

                
            except :
                print('printer error')

            db.child(firmIds[0]+'/invoicePrint').remove()

    if ('certificatePrinter' in metaData['config'] and (message['path']=='/certificatePrinter' or 'certificatePrinter' in message["data"])): 
        data=message["data"]  if message['path']=='/certificatePrinter' else message["data"]['certificatePrinter']
        if(data):  
            try :
                SetPrintingJobCertificate(data)
                lastCheckTime = time.time() #printer refresh

                
            except :
                print('printer error')

            db.child(firmIds[0]+'/certificatePrinter').remove()


    if  ('reportPrinter' in metaData['config'] and (message['path']=='/reportPrinter' or 'reportPrinter' in message["data"])): 
        data=message["data"]  if message['path']=='/reportPrinter' else message["data"]['reportPrinter']
        if(data):  
            try :
                SetPrintingJobReport(data)
                lastCheckTime = time.time() #printer refresh

                
            except :
                print('printer error')

            db.child(firmIds[0]+'/reportPrinter').remove()

    if  ('cashFlowPrinter' in metaData['config'] and (message['path']=='/cashFlowPrinter' or 'cashFlowPrinter' in message["data"])): 
        data=message["data"]  if message['path']=='/cashFlowPrinter' else message["data"]['cashFlowPrinter']
        if(data):  
            # setStatementPrinter(data)
            try :
                setStatementPrinter(data)
                lastCheckTime = time.time() #printer refresh

                
            except :
                print('printer error')

            db.child(firmIds[0]+'/cashFlowPrinter').remove()

    if  ('managePrinter' in metaData['config'] and (message['path']=='/managePrinter' or 'managePrinter' in message["data"])): 
        data=message["data"]  if message['path']=='/managePrinter' else message["data"]['managePrinter']
        if(data):  
            # setDetailBooktPrinter(data)
            try :
                setDetailBooktPrinter(data)
                lastCheckTime = time.time() #printer refresh

                
            except :
                print('printer error')

            db.child(firmIds[0]+'/managePrinter').remove()


    if  ('stockPrinter' in metaData['config'] and len(firmIds) ==1 and (message['path']=='/stockPrinter' or 'stockPrinter' in message["data"])): 
        data=message["data"]  if message['path']=='/stockPrinter' else message["data"]['stockPrinter']
        if(data):  
            try :
                SetPrintingJobStock(data)
                lastCheckTime = time.time() #printer refresh

                
            except :
                print('printer error')

            db.child(firmIds[0]+'/stockPrinter').remove()


db.child(firmIds[0]).stream(mainListener)

if ('stockPrinter' in metaData['config'] and len(firmIds) >1):
    def listener(message):
        data=message["data"]        
        if(data):  
            try:
                SetPrintingJobStock(data)
                lastCheckTime = time.time() #printer refresh

                
            except :
                print('printer error')
            db.child(data['firmID']+'/stockPrinter').remove() 
    
    for firmId in firmIds:
        db.child(firmId+'/stockPrinter').stream(listener)




#if ('printerRefresh' in metaData and metaData['printerRefresh']):
print ('Printer Refresh')
metaData['printerRefresh']= metaData['printerRefresh'] if 'printerRefresh' in metaData and metaData['printerRefresh'] else 25
while (True):
    if(time.time()>lastCheckTime+int(metaData['printerRefresh'])*60):
        lastCheckTime = time.time()
        os.system('lpstat -t')
        print ('Printer Refresh')
    time.sleep(60)
        

        
