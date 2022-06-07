import io
from functions import currencyFormater
from reportlab.pdfgen import canvas
import os



def setDetailBooktPrinter (printData ):
    pdf_file = 'destination.pdf'
 
    can = canvas.Canvas(pdf_file)
    no=1
    page=0

    
    top=830
    lSpace=14   
    l=1
    page+=1   

    can.setFont("Helvetica-Bold", 11)
    can.drawString(40, top-l*lSpace, 'PAGE : '+str(page) )
    can.drawRightString(570, top-l*lSpace,"PRINTED ON : "+ printData['printedOn'])
    l+=1.5
    can.setFont("Helvetica-Bold", 16)
    can.drawString(90, top-l*lSpace, 'EXTRANEOUS TRASNSACTION BOOK' )#80      
    l+=1.5
    can.setFont("Helvetica-Bold", 12)
    can.drawString(40, top-l*lSpace, 'No.' )
    can.drawString(90, top-l*lSpace, 'Description' )
    can.drawString(440, top-l*lSpace, 'Credit' )
    can.drawString(530, top-l*lSpace, 'Debit' )
    l+=1.5

    if ('otherIncome' in printData):
        can.setFont("Helvetica-Bold", 11)
        can.drawString(90, top-l*lSpace, 'OTHER INCOME DETAILS' )#80   
        l+=1
        can.setFont("Helvetica", 11)
        for (key, value) in printData['otherIncome'].items():
            if (top-l*lSpace-2*lSpace<0):
                top=830
                lSpace=14   
                l=1
                page+=1   

                can.setFont("Helvetica-Bold", 11)
                can.drawString(40, top-l*lSpace, 'PAGE : '+str(page) )
                can.drawRightString(570, top-l*lSpace,"PRINTED ON : "+ printData['printedOn'])
                l+=1.5
                can.setFont("Helvetica-Bold", 16)
                can.drawString(90, top-l*lSpace, 'EXTRANEOUS TRASNSACTION CONTINUE..' )#80      
                l+=1.5
                can.setFont("Helvetica-Bold", 12)
                can.drawString(40, top-l*lSpace, 'No.' )
                can.drawString(90, top-l*lSpace, 'Description' )
                can.drawString(440, top-l*lSpace, 'Credit' )
                can.drawString(530, top-l*lSpace, 'Debit' )
                l+=1.5



            can.drawString(30, top-l*lSpace, "{:^12}".format( str(no)))
            can.drawString(90, top-l*lSpace, key)#80   
            
            can.drawRightString(480, top-l*lSpace, currencyFormater(value)+'.00' )
            can.drawRightString(570, top-l*lSpace, '' )
            l+=1
            no+=1 
    l+=0.5
    if ('expense' in printData):
        can.setFont("Helvetica-Bold", 11)
        can.drawString(90, top-l*lSpace, 'EXPENSE DETAILS' )#80   
        l+=1
        can.setFont("Helvetica", 11)
        for (key, value) in printData['expense'].items():
            if (top-l*lSpace-2*lSpace<0):
                top=830
                lSpace=14   
                l=1
                page+=1   

                can.setFont("Helvetica-Bold", 11)
                can.drawString(40, top-l*lSpace, 'PAGE : '+str(page) )
                can.drawRightString(570, top-l*lSpace,"PRINTED ON : "+ printData['printedOn'])
                l+=1.5
                can.setFont("Helvetica-Bold", 16)
                can.drawString(90, top-l*lSpace, 'EXTRANEOUS TRASNSACTION CONTINUE..' )#80      
                l+=1.5
                can.setFont("Helvetica-Bold", 12)
                can.drawString(40, top-l*lSpace, 'No.' )
                can.drawString(90, top-l*lSpace, 'Description' )
                can.drawString(440, top-l*lSpace, 'Credit' )
                can.drawString(530, top-l*lSpace, 'Debit' )
                l+=1.5
            can.drawString(30, top-l*lSpace, "{:^12}".format( str(no)))
            can.drawString(90, top-l*lSpace, key)#80   
            
            can.drawRightString(450, top-l*lSpace, '' )
            can.drawRightString(570, top-l*lSpace, currencyFormater(value)+'.00' )
            l+=1
            no+=1 

    l+=0.5
    if ('otherPays' in printData):
        can.setFont("Helvetica-Bold", 11)
        can.drawString(90, top-l*lSpace, 'OTHER PAYMENTS DETAILS' )#80   
        l+=1
        can.setFont("Helvetica", 11)
        for (key, value) in printData['otherPays'].items():
            if (top-l*lSpace-2*lSpace<0):
                top=830
                lSpace=14   
                l=1
                page+=1   

                can.setFont("Helvetica-Bold", 11)
                can.drawString(40, top-l*lSpace, 'PAGE : '+str(page) )
                can.drawRightString(570, top-l*lSpace,"PRINTED ON : "+ printData['printedOn'])
                l+=1.5
                can.setFont("Helvetica-Bold", 16)
                can.drawString(90, top-l*lSpace, 'EXTRANEOUS TRASNSACTION CONTINUE..' )#80      
                l+=1.5
                can.setFont("Helvetica-Bold", 12)
                can.drawString(40, top-l*lSpace, 'No.' )
                can.drawString(90, top-l*lSpace, 'Description' )
                can.drawString(440, top-l*lSpace, 'Credit' )
                can.drawString(530, top-l*lSpace, 'Debit' )
                l+=1.5
            can.drawString(30, top-l*lSpace, "{:^12}".format( str(no)))
            can.drawString(90, top-l*lSpace, key)#80   
            
            can.drawRightString(450, top-l*lSpace, '' )
            can.drawRightString(570, top-l*lSpace, currencyFormater(value)+'.00' )
            l+=1
            no+=1 
    


    can.save()

    #move to the beginning of the StringIO buffer
  
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

