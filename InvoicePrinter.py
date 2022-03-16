from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from functions import currencyFormater
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



def setPDFInvoicePrinter (printer,printingHeader,printData ):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    cusPhone = printData['namePhone'] if ('namePhone' in printData and printData['namePhone']) else '--'
    cusAdress =  printData['nameAddress'] if 'nameAddress' in printData else '--' 

    printValue = printData['printValue'] if 'printValue' in printData else True 

    if int(printData['balance'])>0 :
        invType = 'A/C'+' '+printData['type'] 
    elif (int(printData['balance'])==0 and printData['type'] in ['Sales', 'Sales_Saved']):  
        invType = 'Cash'+' '+printData['type']
    else:
        invType =printData['type']

    can.setFont("Helvetica", 11)

    can.drawString(410, 820, "DATE")
    can.drawString(450, 820, ": "+printData['date']+' '+ printData['time'][0:5] +' '+printData['time'][-2:])

    can.drawString(440, 720, "No. : "+printData['invoiceSN'])
    # can.drawString(430, 4, ": "+printData['invoiceSN'])

    can.drawString(70, 646, "NAME  : "+printData['name'].upper())

    can.drawString(255, 646, "PHONE  : "+cusPhone)

    can.drawRightString(520, 646, "NIC  : "+printData['nameNIC'])

    can.setFont("Helvetica", 11)
    

    

    # can.drawString(370, 548, "Inv. Type")
    # can.drawString(430, 548, ": "+invType.upper())

    # can.drawString(370, 533, "Issued by")
    # can.drawString(430, 533, ": "+printData['issuedby'])


   

    if (printData['type']=='Paid'):
        comment = "("+printData['comment']+')' if ('comment' in printData and  printData['comment'] and printData['comment']!='Nothing' ) else ' '
        can.setFont("Helvetica", 13)
        can.drawString(37, 460, "{:^12}".format( '1'))
        can.drawString(80, 460, 'A PAYMENT RECEIVED-CONFIRMATION' )
        can.drawString(340, 460,"{:^32}".format( printData['payMethod']))
        can.drawRightString(570, 460, currencyFormater(printData['total'])+'.00')
        can.setFont("Helvetica", 11)
        can.drawString(80, 444, comment )

        can.setFont("Helvetica", 13)
        can.drawRightString(565, 210, 'Rs. '+currencyFormater(float(printData['total']))+'0')
        

    else :
        can.setFont("Helvetica", 10)
        i=0
        for (key, value) in printData['itemList'].items():
            y=600-i*15
            i=i+1
            can.drawString(63, y, "{:^12}".format( str(i)))
            can.drawString(105, y, value['label'].upper() )#80
            can.drawString(360, y, "{:^18}".format( str(value['weight'])+'g'))
            if (printValue):
                can.drawRightString(530, y,  currencyFormater(float(value['unitPrice'])*float(value['quantity']))+'0')



        if (printData['purchase']):
            can.setFont("Helvetica-Bold", 10)
            y= 520
            if (i!=0 and printValue):
                i=0
                can.drawString(360, y-i*15, "{:<18}".format( 'TOTAL'))
                can.drawRightString(530, y-i*15,currencyFormater(float(printData['total']))+'0')
            i=0
            
            
            i=i+1
            can.drawString(105, y-i*15, 'PAYMENTS' )

            i=i+1

            can.setFont("Helvetica", 10)
            
            can.drawString(105, y-i*15, printData['payMethod1'].upper() +' (' +printData['purchase']+')')#80
            #can.drawString(360, y-i*15, "{:^18}".format( str(value['weight'])+'g'))
            if(printValue):
                can.drawRightString(530, y-i*15, '('+ currencyFormater(float(printData['payAmount'])-float(printData['payMethod2Amount']))+'0)')


            i=i+1
            can.drawString(105, y-i*15, printData['payMethod2'].upper() )#80
            #can.drawString(360, y-i*15, "{:^18}".format( str(value['weight'])+'g'))
            if(printValue):
                can.drawRightString(530, y-i*15, '('+ currencyFormater(float(printData['payMethod2Amount']))+'0)')

            can.setFont("Helvetica-Bold", 12)
            can.drawRightString(520, 444, 'Rs. '+currencyFormater(float(printData['balance']))+'0')

        else :             
            can.setFont("Helvetica-Bold", 10)
            can.drawString(360, 495, "{:<18}".format( 'TOTAL'))
            can.drawRightString(530,495,currencyFormater(float(printData['total']))+'0')
            can.drawString(360, 480, "{:<18}".format( 'PAID'))
            can.drawRightString(530, 480,'('+currencyFormater(float(printData['payAmount']))+'0)')

            can.setFont("Helvetica-Bold", 12)
            can.drawRightString(520, 444, 'Rs. '+currencyFormater(float(printData['balance']))+'0')


        

    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("invTemp.pdf", "rb")) if (printData['type']=='Paid') else PdfFileReader(open("invTemp.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("destination.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    #os.system('lp ./destination.pdf')


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