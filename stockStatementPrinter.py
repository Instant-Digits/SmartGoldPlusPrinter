from tracemalloc import start
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from functions import currencyFormater,nameDecode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter




def setStockStatementPrinter(printData):

 
    pdf_file = 'destination.pdf'
 
    can = canvas.Canvas(pdf_file)

    

    y=770 #800
    l =0
    lSpace=13
    page =1


    typeInv = printData['type'] if ('type' in printData and printData['type']) else '--'
    can.setFont("Helvetica", 11)
    can.drawString(60, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+printData['firmCode']+'    TYPE : '+typeInv+ "    DATE : "+ printData['printedOn'])
    l+=1
    l+=1

    can.setFont("Helvetica-Bold", 12)
    can.drawString(50, y-l*lSpace,'ITEMS')
    can.drawString(190, y-l*lSpace,'INITAL')
    can.drawString(290, y-l*lSpace,'SOLD (-)')
    can.drawString(390, y-l*lSpace,'ADDED (+)')
    can.drawString(490, y-l*lSpace,'FINAL')
    l+=1
    l+=1

    for (key, value) in printData.items():
        if (y-l*lSpace-5*lSpace<0):
            can.showPage()
            y=800
            l =0
            page+=1
            can.drawString(60, y-l*lSpace,'Page No : '+str(page)+'    Type : '+typeInv+ "      Printed on : "+ printData['printedOn'])
            l+=1
            l+=1
            can.setFont("Helvetica-Bold", 12)
            can.drawString(50, y-l*lSpace,'ITEMS')
            can.drawString(190, y-l*lSpace,'INITAL')
            can.drawString(290, y-l*lSpace,'SOLD (-)')
            can.drawString(390, y-l*lSpace,'ADDED (+)')
            can.drawString(490, y-l*lSpace,'FINAL')
            l+=1
            l+=1


        if (type(value) is dict):
            can.setFont("Helvetica-Bold", 10)
            can.drawString(40, y-l*lSpace, nameDecode(key))
            startQts = value['count']['final']['qts']+value['count']['sold']['qts']-value['count']['added']['qts']
            startWeight = float(value['count']['final']['weight'])+float(value['count']['sold']['weight'])-float(value['count']['added']['weight'])
            can.drawRightString(210, y-l*lSpace,currencyFormater(startQts)+' | ')
            can.drawString(210, y-l*lSpace,currencyFormater(startWeight)+'g')

            can.drawRightString(310, y-l*lSpace,currencyFormater(value['count']['sold']['qts'])+' | ')
            can.drawString(310, y-l*lSpace,currencyFormater(value['count']['sold']['weight'])+'g')

            can.drawRightString(410, y-l*lSpace,currencyFormater(value['count']['added']['qts'])+' | ')
            can.drawString(410, y-l*lSpace,currencyFormater(value['count']['added']['weight'])+'g')

            can.drawRightString(510, y-l*lSpace,currencyFormater(value['count']['final']['qts'])+' | ')
            can.drawString(510, y-l*lSpace,currencyFormater(value['count']['final']['weight'])+'g')
            
            # can.drawString(180, y-l*lSpace,currencyFormater(startQts)+'| '+currencyFormater(startWeight)+'g')
            # can.drawString(290, y-l*lSpace,currencyFormater(value['count']['sold']['qts'])+'| '+currencyFormater(value['count']['sold']['weight'])+'g')
            # can.drawString(390, y-l*lSpace,currencyFormater(value['count']['added']['qts'])+'| '+currencyFormater(value['count']['added']['weight'])+'g')
            # can.drawString(490, y-l*lSpace,currencyFormater(value['count']['final']['qts'])+'| '+currencyFormater(value['count']['final']['weight'])+'g')
            l+=1
            for (key2, value2) in value.items():
                if (y-l*lSpace-5*lSpace<0):
                    can.showPage()
                    y=800
                    l =0
                    page+=1
                    can.drawString(60, y-l*lSpace,'Page No : '+str(page)+'    Type : '+typeInv+ "      Printed on : "+ printData['printedOn'])
                    l+=1
                    l+=1

                    can.setFont("Helvetica-Bold", 12)
                    can.drawString(50, y-l*lSpace,'ITEMS')
                    can.drawString(190, y-l*lSpace,'INITAL')
                    can.drawString(290, y-l*lSpace,'SOLD (-)')
                    can.drawString(390, y-l*lSpace,'ADDED (+)')
                    can.drawString(490, y-l*lSpace,'FINAL')
                    l+=1
                    l+=1


                
                if (type(value2) is dict and key2 != 'count'):    
                    can.setFont("Helvetica", 9)
                    can.drawString(50, y-l*lSpace, nameDecode(key2))
                    startQts = value2['final']['qts']+value2['sold']['qts']-value2['added']['qts']
                    startWeight = float(value2['final']['weight'])+float(value2['sold']['weight'])-float(value2['added']['weight'])
                    can.drawRightString(210, y-l*lSpace,currencyFormater(startQts)+' | ')
                    can.drawString(210, y-l*lSpace,currencyFormater(startWeight)+'g')

                    can.drawRightString(310, y-l*lSpace,currencyFormater(value2['sold']['qts'])+' | ')
                    can.drawString(310, y-l*lSpace,currencyFormater(value2['sold']['weight'])+'g')
                    
                    can.drawRightString(410, y-l*lSpace,currencyFormater(value2['added']['qts'])+' | ')
                    can.drawString(410, y-l*lSpace,currencyFormater(value2['added']['weight'])+'g')

                    can.drawRightString(510, y-l*lSpace,currencyFormater(value2['final']['qts'])+' | ')
                    can.drawString(510, y-l*lSpace,currencyFormater(value2['final']['weight'])+'g')                    
                    
                    l+=1
        l+=1           
           
                                    



    can.save()

    return('destination.pdf')


#SetPrintingJobCertificate('')


