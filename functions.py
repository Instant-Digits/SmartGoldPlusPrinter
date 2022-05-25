from textwrap import wrap
from escpos.connections import getUSBPrinter
import time


def currencyFormater (num):
    num=str(num)
    prefix = '-' if num[0]=='-' else ''
    num = num[1:]if num[0]=='-' else num
   
    desimalIndex= str(num).find('.')
    if desimalIndex>-1:
        list = wrap(str(num)[desimalIndex-1::-1], 3)
        return prefix+','.join(list)[::-1]+str(num)[desimalIndex:desimalIndex+3] 
    list = wrap(str(num)[::-1], 3)
    
    return   prefix+ ','.join(list)[::-1]

def configPrinters (configData):
    printers={}
    if ('config' in configData.keys()):
        printerConfig =configData['config']
        for (key, value) in printerConfig.items():
            try:
                printers[key] = getUSBPrinter()(idVendor=int(value['idVendor'],16),  # USB vendor and product Ids for Bixolon SRP-350plus
                                                idProduct=int(value['idProduct'],16),  # printer
                                                inputEndPoint=int(value['inputEndPoint'],16),
                                                outputEndPoint=int(value['outputEndPoint'],16))
                print (key+' DETECTED')
            except RuntimeError:
                print (key+' NOT DETECTED')
                return False
        return printers
    return (False)

def configPrinter (printerInfo, name='Printer', timeOut=5):
    timeStart = time.time()
    timeOut=timeOut*60
    while (True):
        try:
            printer = getUSBPrinter()(idVendor=int(printerInfo['idVendor'],16),  # USB vendor and product Ids for Bixolon SRP-350plus
                                            idProduct=int(printerInfo['idProduct'],16),  # printer
                                            inputEndPoint=int(printerInfo['inputEndPoint'],16),
                                            outputEndPoint=int(printerInfo['outputEndPoint'],16))
            print (name+' DETECTED')
            return printer
        except RuntimeError:
            print (name+' NOT DETECTED')
            print ('Waiting For '+name)
            time.sleep(5)
            if (time.time()>timeStart+timeOut):
                print ("waiting timeout for printer Search")
                return False
            
        

def nameDecode (str1):
    return (str1 or '').replace('&&','.')