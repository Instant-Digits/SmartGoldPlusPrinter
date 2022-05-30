from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from functions import currencyFormater
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os



def setStatementPrinter (printData ):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    
    top=650
    lSpace=20   
    l=1
   

    can.drawRightString(520, 750,"PRINTED ON : "+ printData['printedOn'])

    can.setFont("Helvetica-Bold", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l)))
    can.drawString(140, top-l*lSpace, 'INITIAL CASH BALANCE' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['initialCashBalance'])+'.00' )

    l+=1

    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l)))
    can.drawString(140, top-l*lSpace, 'SALES BY CASH' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['cashSales'])+'.00' )


    l+=1
    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l)))
    can.drawString(140, top-l*lSpace, '(A/C) ADVANCE')#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['acSalesCash'])+'.00' )

    l+=1
    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l)))
    can.drawString(140, top-l*lSpace, '(A/C) PAYMENT RECEIVED' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['cusPaymentSales'])+'.00' )

    l+=1
    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l)))
    can.drawString(140, top-l*lSpace, 'CASH ORDER' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['orderCash'])+'.00' )

    l+=1
    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l)))
    can.drawString(140, top-l*lSpace, 'ORDER PAYMENT RECEIVED' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['cusPaymentOrder'])+'.00' )

    l+=1
    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l)))
    can.drawString(140, top-l*lSpace, 'OTHER INCOME CASH' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['otherIncome'])+'.00' )
    l+=1
    can.drawRightString(530, top-l*lSpace,'_______________' )
    
    l+=1
    can.setFont("Helvetica-Bold", 12)
    can.drawString(140, top-l*lSpace, 'TOTAL CASH INFLOW' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['cashIn'])+'.00' )


    l+=1
    l+=1

    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l-3)))
    can.drawString(140, top-l*lSpace, 'PAYMENT FOR CUSTOMER PURCHASE' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['paidPurchase'])+'.00' )


    # l+=1
    # can.setFont("Helvetica", 12)
    # can.drawString(80, top-l*lSpace, "{:^12}".format( str(l-3)))
    # can.drawString(140, top-l*lSpace, 'PAID AS PURCHASE/ORDER BALANCE' )#80   

    # can.drawRightString(520, top-l*lSpace, currencyFormater(printData['paidBalanceP_O'])+'.00' )

    l+=1
    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l-3)))
    can.drawString(140, top-l*lSpace, 'EXPENSE BY CASH' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['expense'])+'.00' )

    l+=1
    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l-3)))
    can.drawString(140, top-l*lSpace, 'BANK DEPOSIT' )#80   
    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['bank'])+'.00' )

    l+=1
    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l-3)))
    can.drawString(140, top-l*lSpace, 'OTHER SAVINGS' )#80   
    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['otherSaving'])+'.00' )

    l+=1
    can.setFont("Helvetica", 12)
    can.drawString(80, top-l*lSpace, "{:^12}".format( str(l-3)))
    can.drawString(140, top-l*lSpace, 'OTHER PAYMENTS' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['otherPayments'])+'.00' )
    l+=1
    can.drawRightString(530, top-l*lSpace,'_______________' )
    
    l+=1
    can.setFont("Helvetica-Bold", 12)
    can.drawString(140, top-l*lSpace, 'TOTAL CASH OUTFLOW' )#80   

    can.drawRightString(520, top-l*lSpace, currencyFormater(printData['cashOut'])+'.00' )
   
    l+=1
    can.setFont("Helvetica", 12)
    can.drawRightString(530, top-l*lSpace,'_______________' )
   
    l+=1
    can.setFont("Helvetica-Bold", 13)
    can.drawString(140, top-l*lSpace-5, 'EDNING BALANCE' )#80   

    can.drawRightString(520, top-l*lSpace-5, currencyFormater(printData['balance'])+'.00' )
    can.setFont("Helvetica", 12)

    can.drawRightString(530, top-l*lSpace-10,'_______________' )
    can.drawRightString(530, top-l*lSpace-12,'_______________' )
    
            
      


        

    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("cashflowStatement.pdf", "rb")) 
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("destination.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
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

