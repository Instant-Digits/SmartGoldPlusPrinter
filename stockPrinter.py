from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from functions import currencyFormater,nameDecode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter




def SetPrintingJobStock(printData):

 
    pdf_file = 'stockPDF.pdf'
 
    can = canvas.Canvas(pdf_file)

    

    y=800
    l =0
    lSpace=15
    page =1


    typeInv = printData['type'] if ('type' in printData and printData['type']) else '--'

    can.drawString(60, y-l*lSpace,'Page No : '+str(page)+'    Type : '+typeInv+ "      Printed on : "+ printData['printedOn'])
    l+=1
    l+=1

    for (key, value) in printData.items():
        if (y-l*lSpace-lSpace<0):
            can.showPage()
            y=800
            l =0
            page+=1
            can.drawString(60, y-l*lSpace,'Page No : '+str(page)+'    Type : '+typeInv+ "      Printed on : "+ printData['printedOn'])
            l+=1
            l+=1


        if (type(value) is dict):
            can.setFont("Helvetica-Bold", 12)
            can.drawString(60, y-l*lSpace, nameDecode(key)+ '  : '+ currencyFormater(value['qts'])+'  || W : '+ currencyFormater(value['weight'])+'g')
            l+=1
            for (key2, value2) in value.items():
                if (y-l*lSpace-lSpace<0):
                    can.showPage()
                    y=800
                    l =0
                    page+=1
                    can.drawString(60, y-l*lSpace,'Page No : '+str(page)+'    Type : '+typeInv+ "      Printed on : "+ printData['printedOn'])
                    l+=1
                    l+=1



                if (type(value2) is dict):
                    can.setFont("Helvetica-Bold", 11)

                    can.drawString(80, y-l*lSpace, nameDecode(key2) +'  : '+ currencyFormater(value2['qts'])+'  || W : '+ currencyFormater(value2['weight'])+'g')        
                    l+=1
                    for (key3, value3) in value2.items():
                        
                        if (y-l*lSpace-lSpace<0):
                            can.showPage()
                            y=800
                            l =0
                            page+=1
                            can.drawString(60, y-l*lSpace,'Page No : '+str(page)+'    Type : '+typeInv+ "      Printed on : "+ printData['printedOn'])
                            l+=1
                            l+=1
                            can.setFont("Helvetica-Bold", 12)
                            can.drawString(100, y-l*lSpace, 'Continued..')
                            l+=1

                        if (type(value3) is dict):
                            can.setFont("Helvetica", 10)

                            can.drawString(100, y-l*lSpace, nameDecode(key3))
                            can.drawString(340, y-l*lSpace, ': '+ currencyFormater(value3['qts'])+'  || W : '+ currencyFormater(value3['weight'])+'g')        
        


    can.save()

    #os.system('lp ./stockPDF.pdf')


#SetPrintingJobCertificate('')


def create_pdf():
    pdf_file = 'multipage.pdf'
 
    can = canvas.Canvas(pdf_file)
 
    can.drawString(20, 800, "First Page")
    can.showPage()
 
    can.drawString(20, 800, "Second Page")
    can.showPage()
 
    can.drawString(20, 700, "Third Page")
    can.showPage()
 
    can.save()
 
