from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from functions import currencyFormater
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os



def setStatementPrinter (printData ):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    
    top=680
    lSpace=20   
    l=1
   

    can.drawRightString(570, 760,"PRINTED ON : "+ printData['printedOn'])

    can.setFont("Helvetica-Bold", 12)
    can.drawString(40, top-l*lSpace, "{:^12}".format( str(l)))
    can.drawString(90, top-l*lSpace, 'INITIAL BALANCES' )#80   

    can.drawRightString(450, top-l*lSpace, currencyFormater(printData['initialCashBalance'])+'.00' )
    can.drawRightString(570, top-l*lSpace, currencyFormater(printData['initialBalance'] if 'initialBalance' in printData else 0)+'.00' )


    l+=1
    l+=1
    can.drawString(90, top-l*lSpace, 'INFLOW DETAILS' )#80   
    l+=1
    can.setFont("Helvetica", 12)
    totalInflow=0
    for flowIn in printData['cashInFlows']:
        can.drawString(40, top-l*lSpace, "{:^12}".format( str(l-1)))
        can.drawString(90, top-l*lSpace, flowIn['label']+( ' ('+ flowIn['info'] +')' if flowIn['info'] else ''))#80   
        totalInflow+=flowIn['total']
        can.drawRightString(450, top-l*lSpace, currencyFormater(flowIn['cash'])+'.00' )
        can.drawRightString(570, top-l*lSpace, currencyFormater(flowIn['total'])+'.00' )
        l+=1

    
    can.drawRightString(450, top-l*lSpace,'_____________' )
    can.drawRightString(570, top-l*lSpace,'_____________' )
    
    l+=1
    can.setFont("Helvetica-Bold", 12)
    can.drawString(100, top-l*lSpace, 'TOTAL INFLOW' )#80   

    can.drawRightString(450, top-l*lSpace, currencyFormater(printData['cashIn'])+'.00' )
    can.drawRightString(570, top-l*lSpace, currencyFormater(totalInflow)+'.00' )


    l+=1
    l+=1

    can.drawString(90, top-l*lSpace, 'OUTFLOW (PAID) DETAILS' )#80   
    l+=1
    can.setFont("Helvetica", 12)
    totalOutflow=0
    for flowIn in printData['cashOutFlows']:
        can.drawString(40, top-l*lSpace, "{:^12}".format( str(l-5)))
        can.drawString(90, top-l*lSpace, flowIn['label']+( ' ('+ flowIn['info'] +')' if flowIn['info'] else ''))#80   
        totalOutflow+=flowIn['total']
        can.drawRightString(450, top-l*lSpace, currencyFormater(flowIn['cash'])+'.00' )
        can.drawRightString(570, top-l*lSpace, currencyFormater(flowIn['total'])+'.00' )
        l+=1

    
    can.drawRightString(450, top-l*lSpace,'_____________' )
    can.drawRightString(570, top-l*lSpace,'_____________' )
    
    l+=1

    can.setFont("Helvetica-Bold", 12)
    can.drawString(100, top-l*lSpace, 'TOTAL OUTFLOW' )#80   

    can.drawRightString(450, top-l*lSpace, currencyFormater(printData['cashOut'])+'.00' )
    can.drawRightString(570, top-l*lSpace, currencyFormater(totalOutflow)+'.00' )


    l+=1
    can.setFont("Helvetica", 12)
    can.drawRightString(450, top-l*lSpace,'_____________' )
    can.drawRightString(570, top-l*lSpace,'_____________' )
   
    l+=1
    can.setFont("Helvetica-Bold", 13)
    can.drawString(100, top-l*lSpace-5, 'CLOSING BALANCES' )#80   

    can.drawRightString(450, top-l*lSpace-5, currencyFormater(printData['balance'])+'.00' )
    can.drawRightString(570, top-l*lSpace-5, currencyFormater((printData['initialBalance'] if 'initialBalance' in printData else 0)+totalInflow-totalOutflow)+'.00' )

    can.setFont("Helvetica", 12)
    can.drawRightString(450, top-l*lSpace-10,'_____________' )
    can.drawRightString(450, top-l*lSpace-12,'_____________' )
    can.drawRightString(570, top-l*lSpace-10,'_____________' )
    can.drawRightString(570, top-l*lSpace-12,'_____________' )


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

