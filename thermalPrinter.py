from functions import currencyFormater

def setThermalPrinting(printer,  printingHeader,printData):     

    #Header
    printer.align('center')
    printer.bold()
    printer.text(printingHeader['name'].upper())
    printer.lf()
    printer.bold(False)


    printer.text(printingHeader['address'])
    printer.lf()	
    printer.text(printingHeader['tp'])
    printer.lf()
    printer.text('Invoice No :- '+printData['invoiceSN'])
    printer.lf()

    printer.lf()
    printer.align('left')
    printer.text(printData['date'] +'@'+printData['time']+' -- '+printData['name']+' -- '+printData['type'])
    printer.lf()

   
    #print Bill
    if (printData['type']=='Paid'):
        printer.lf()
        printer.align('center')
        printer.text ("{:<1} {:<25} {:<14}".format('','PAYMENT METHOD',printData['payMethod']))        
        printer.lf()
        printer.text ("{:<1} {:<25} {:<14}".format('','RECEIVED AMOUNT','Rs. '+currencyFormater(printData['total'])))        
        printer.lf()
        printer.text ("{:<1} {:<25} {:<14}".format('','RECEIVED BY',printData['issuedby']))        
        printer.lf()
        printer.lf()
        printer.text('THANK YOU FOR YOUR PAYMENT !');
        printer.lf()
      

    else: 
        for (key, value) in printData['itemList'].items():
            printer.align('left');
            printer.text(value['make']+' '+value['item'] );
            printer.lf();
            printer.align('right')
            printer.text ("{:<1} {:<20} {right_aligned:>15}".format(' ', 
                    str(value['quantity']) +' x Rs.'+currencyFormater(value['unitPrice']), 
                    right_aligned='Rs.'+currencyFormater(float(value['unitPrice'])*float(value['quantity']))
                    ));
            printer.lf()
        printer.text ('')
        printer.lf()
        printer.text ("{:<1} {:<10} {:<14}".format('','TOTAL','Rs. '+currencyFormater(float(printData['total']))))
        printer.lf();
    
    printer.lf()
    printer.lf()
    printer.align('center')
    printer.text(' ------------------------------------------ ')
    printer.lf()
    printer.invert()
    printer.text(' POWERED BY INSTANT DIGITS (PVT) LTD ')
    printer.lf()
    printer.text(' Call us on 071 999 2075 ')
    printer.lf()
    printer.invert(False)


    printer.lf()
    printer.lf()
    printer.lf()
    printer.lf()
        
    printer.text('\x1dV\x00')




# printer = getUSBPrinter()(idVendor=0x0483,  # USB vendor and product Ids for Bixolon SRP-350plus
#                   idProduct=0x5743,  # printer
#                   inputEndPoint=0x82,
#                   outputEndPoint=0x01)
