from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from functions import currencyFormater
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os



def setPDFInvoicePrinter (printData ):
    # packet = io.BytesIO()
    # can = canvas.Canvas(packet, pagesize=letter)

    pdf_file = 'destination.pdf'
 
    can = canvas.Canvas(pdf_file)

    cusPhone = printData['namePhone'] if ('namePhone' in printData and printData['namePhone']) else '--'
    cusAdress =  printData['nameAddress'] if 'nameAddress' in printData else '--' 

   

    printValue = not(printData['hideValue']) if 'hideValue' in printData else True 
    

    if int(printData['balance'])>0 :
        invType = 'A/C'+' '+printData['type'] 
    elif (int(printData['balance'])==0 and printData['type'] in ['Sales', 'Sales_Saved']):  
        invType = 'Cash'+' '+printData['type']
    else:
        invType =printData['type']

    can.setFont("Helvetica", 10)

    can.drawString(410, 828, "DATE")
    can.drawString(450, 828, ": "+printData['date']+' '+ printData['time'][0:5] +' '+printData['time'][-2:])
    
    can.setFont("Helvetica", 11)
    can.drawString(55, 716, "No. : "+printData['invoiceSN'])
    # can.drawString(430, 4, ": "+printData['invoiceSN'])

    can.drawString(235, 716, "NAME  : "+printData['name'].upper())

    can.drawRightString(535, 716, "PHONE  : "+cusPhone)

    #can.drawRightString(520, 638, "NIC  : "+(printData['nameNIC'] or '--'))

    can.setFont("Helvetica", 11)
    

    

    # can.drawString(370, 548, "Inv. Type")
    # can.drawString(430, 548, ": "+invType.upper())

    # can.drawString(370, 533, "Issued by")
    # can.drawString(430, 533, ": "+printData['issuedby'])


   

    if (printData['type']=='Paid'):
        can.setFont("Helvetica-Bold", 11)
         
        can.drawString(58, 690, 'No.' )
        can.drawString(176, 690, 'Description' )
        # can.drawString(332, 690, 'Karat' )
        can.drawString(390, 690, 'Method' )
        can.drawString(465, 690, 'Amount (Rs)' )

        comment = "("+printData['comment']+')' if ('comment' in printData and  printData['comment'] and printData['comment']!='Nothing' ) else ' '
        can.setFont("Helvetica", 11)
        can.drawString(50, 665, "{:^12}".format( '1'))
        can.drawString(90, 665, 'A PAYMENT RECEIVED-CONFIRMATION' )
        can.drawString(370, 665,"{:^18}".format( printData['payMethod'].upper()))
        can.drawRightString(545, 665, currencyFormater(printData['total'])+'.00')
        can.setFont("Helvetica", 11)
        can.drawString(90, 650, (printData['paidForLabel'] or 'PAID FOR SMS').upper() )
        can.drawString(90, 630, comment )

        can.setFont("Helvetica", 11)
        can.drawString(55, 474, "ISSUED BY : "+printData['issuedby'].upper())

        can.drawString(235, 474, "TYPE : PAYMENT")

        can.setFont("Helvetica-Bold", 12)
        
        can.drawRightString(420, 474, 'TOTAL')

        
        can.drawRightString(540, 474, 'Rs. '+currencyFormater(abs(float(printData['total'])))+'0')

        
        

    else :
        can.setFont("Helvetica-Bold", 11)
         
        can.drawString(58, 690, 'No.' )
        can.drawString(176, 690, 'Description' )
        can.drawString(332, 690, 'Karat' )
        can.drawString(390, 690, 'Weight' )
        can.drawString(465, 690, 'Amount (Rs)' )

        can.setFont("Helvetica", 10)
        i=0
        for (key, value) in printData['itemList'].items():
            y=670-i*14
            i=i+1
            karadUnit = 'K' if ('GOLD' in value['id'].upper()) else ''
            can.drawString(50, y, "{:^12}".format( str(i)))
            can.drawString(90, y, value['label'].upper() )#80
            can.setFont("Helvetica-Bold", 10)
            can.drawString(340, y, str(value['karad'])+karadUnit )
            can.setFont("Helvetica", 10)
            can.drawString(380, y, "{:^18}".format( str(value['weight'])+'g'))
            if (printValue):
                can.drawRightString(545, y,  currencyFormater(float(value['unitPrice'])*float(value['quantity']))+'0')



        if ('purchase' in printData and  printData['purchase']):
            can.setFont("Helvetica-Bold", 10)
            y= 553
            # if (i!=0 and printValue):
            #     i=0
            #     can.drawString(375, y-i*13, "{:<18}".format( 'TOTAL'))
            #     can.drawRightString(545, y-i*13,currencyFormater(float(printData['total']))+'0')
            i=0
            
            
            i=i+1
            can.drawString(90, y-i*13, 'PAYMENTS' )

            i=i+1

            can.setFont("Helvetica", 10)
            
            can.drawString(90, y-i*13, printData['payMethod1'].upper() +' (' +printData['purchase']+')')#80
            #can.drawString(360, y-i*13, "{:^18}".format( str(value['weight'])+'g'))
            if(printValue):
                can.drawRightString(545, y-i*13, '('+ currencyFormater(float(printData['payAmount'])-float(printData['payMethod2Amount']))+'0)')


            i=i+1
            can.drawString(90, y-i*13, printData['payMethod2'].upper() )#80
            #can.drawString(360, y-i*13, "{:^18}".format( str(value['weight'])+'g'))
            
            can.drawRightString(545, y-i*13, '('+ currencyFormater(float(printData['payMethod2Amount']))+'0)')

            i=i+1
            can.drawString(90, y-i*13, 'BALANCE' )#80
            #can.drawString(360, y-i*13, "{:^18}".format( str(value['weight'])+'g'))
            
            can.drawRightString(545, y-i*13, '('+ currencyFormater(float(printData['balance']))+'0)')
          
           

        else :             
            can.setFont("Helvetica-Bold", 10)
            
            can.drawString(380, 510, "{:<18}".format( 'PAID'))
            can.drawRightString(545, 510,'('+currencyFormater(float(printData['payAmount']))+'0)')

            can.drawString(380, 499, "{:<18}".format( 'BALANCE'))
            can.drawRightString(545,499,currencyFormater(float(printData['balance']))+'0')

       
        balPrefix = '- ' if float(printData['balance'])<0 else ''

        can.setFont("Helvetica", 11)
        can.drawString(55, 474, "ISSUED BY : "+printData['issuedby'].upper())

        can.drawString(235, 474, "TYPE : "+invType.upper())

        can.setFont("Helvetica-Bold", 12)
        footerText = 'TOTAL' if printValue else printData['payMethod2'].upper()+' BALANCE'
        can.drawRightString(420, 474, footerText)

        footerValue = printData['total'] if printValue else printData['payMethod2Amount']
        can.drawRightString(540, 474, 'Rs. '+currencyFormater(abs(float(footerValue)))+'0')
        
       


        

    can.save()

    # #move to the beginning of the StringIO buffer
    # packet.seek(0)

    # # create a new PDF with Reportlab
    # new_pdf = PdfFileReader(packet)
    # # read your existing PDF
    # existing_pdf = PdfFileReader(open("defultJewelryInvoice.pdf", "rb")) if (printData['type']=='Paid') else PdfFileReader(open("defultJewelryInvoice.pdf", "rb"))
    # output = PdfFileWriter()
    # # add the "watermark" (which is the new pdf) on the existing page
    # page = existing_pdf.getPage(0)
    # page.mergePage(new_pdf.getPage(0))
    # output.addPage(page)
    # # finally, write "output" to a real file
    # outputStream = open("destination.pdf", "wb")
    # output.write(outputStream)
    # outputStream.close()
    os.system('lp ./destination.pdf')


# from reportlab.pdfgen.canvas import Canvas
# from reportlab.lib.units import inch, mm, cm, pica
# from datetime import date, timedelta

# if __name__ == "__main__":
#     pdf = Canvas("output.pdf")
#     pdf.setFont('Helvetica', 9)

#     master_data = ...
#     start = ...
#     end = ...
#     company = ...
#     today = ...

#     lines = [
#         "Rechnungsdatum: "+'today',
#         "Leistungserbringung: "+ '',
#         "Leistungszeitraum: "+'start'+" - "+'end',
#         "Rechnungsnummer: "+'',
#         "Lieferantennummer: ",
#         "Zahlungsziel: " +str((date.today().replace(day=1) - timedelta(days=1)).day)+ " Tage",
#     ]
#     ys = [600,590,580,570,560,550]
#     width = pdf._pagesize[0]
#     padding = 10 * mm
#     for y, line in zip(ys, lines):
#         pdf.drawRightString(20, y, line)
#     pdf.save()