from functions import generateQRCode

def setLabelPrinting(printer,  printingHeader,printData):     

    
    printer.image(generateQRCode( printData['qr'], [printingHeader['name'],'Weight : '+str(printData['weight']+'g'),
    " ".join(printData['id'].split('_')[ 0: len(printData['id'].split('_'))-1]), 
    'S.P : %'+ str(int(printData['pPercentage'])+ int(printData['profitMargin']))]))

    
    printer.lf()
    printer.lf()  

   



# printer = getUSBPrinter()(idVendor=0x0483,  # USB vendor and product Ids for Bixolon SRP-350plus
#                   idProduct=0x5743,  # printer
#                   inputEndPoint=0x82,
#                   outputEndPoint=0x01)
