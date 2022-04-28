from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from functions import currencyFormater,nameDecode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from collections import OrderedDict


def SetPrintingJobReport(printData):

 
    pdf_file = 'report.pdf'
 
    can = canvas.Canvas(pdf_file)

    

    y=800
    l =0
    lSpace=14
    page =1


    can.setFont("Helvetica-Bold", 10)

    date = printData['date'] if ('date' in printData and printData['date']) else '--'

    can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'SALES'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
    l+=1
    l+=1

    can.drawString(20, y-l*lSpace, 'INVOICE NO.')     
    can.drawString(120, y-l*lSpace, 'CUS DETAILS')     
    can.drawString(220, y-l*lSpace, 'ITEMS')        
    can.drawString(370, y-l*lSpace, 'WEIGHT')        
    can.drawString(420, y-l*lSpace, 'SOLD P')  
    can.drawString(490, y-l*lSpace, 'TOTAL') 

    can.drawString(535, y-l*lSpace, 'PAYMENT')        
    l+=1

    can.setFont("Helvetica", 10)
    totalSales=0
    totalPayment=0
    totalUnitPrice=0

    for (key, value) in  dict(sorted(printData['salesItems'].items())).items() :

        if (y-(l+4)*lSpace<0):
            can.showPage()
            y=800
            l =0
            page+=1
            can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'SALES'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
            l+=1
            l+=1
            can.drawString(20, y-l*lSpace, 'INVOICE NO.')     
            can.drawString(120, y-l*lSpace, 'CUS DETAILS')     
            can.drawString(220, y-l*lSpace, 'ITEMS')        
            can.drawString(370, y-l*lSpace, 'WEIGHT')        
            can.drawString(420, y-l*lSpace, 'SOLD P')  
            can.drawString(490, y-l*lSpace, 'TOTAL') 

            can.drawString(535, y-l*lSpace, 'PAYMENT')        
            l+=1

        can.drawString(20, y-l*lSpace, value['invoiceSN'])     
        can.drawString(120, y-l*lSpace, value['name'])            
               
        can.drawRightString(525, y-l*lSpace, currencyFormater(value['total']))        
        can.drawRightString(580, y-l*lSpace, currencyFormater(value['payAmount']))  
        
        totalSales = value['total']+totalSales
        totalPayment = value['payAmount']+totalPayment

        
        invLine=1
        for (key2, value2) in  value['itemList'].items():
            # if (invLine==2):
            #     can.drawString(120, y-l*lSpace, value['namePhone'])
            if (y-(l+4)*lSpace<0):
                can.showPage()
                y=800
                l =0
                page+=1
                can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'SALES'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                l+=1
                l+=1
                can.drawString(20, y-l*lSpace, 'INVOICE NO.')     
                can.drawString(120, y-l*lSpace, 'CUS DETAILS')     
                can.drawString(220, y-l*lSpace, 'ITEMS')        
                can.drawString(370, y-l*lSpace, 'WEIGHT')        
                can.drawString(420, y-l*lSpace, 'SOLD P')  
                can.drawString(490, y-l*lSpace, 'TOTAL') 

                can.drawString(535, y-l*lSpace, 'PAYMENT')        
                l+=1

            can.drawString(220, y-l*lSpace, (value2['label'][:30] + '..') if len(value2['label']) > 30 else value2['label'] )        
            can.drawRightString(410, y-l*lSpace, value2['weight']+'g')
            can.drawRightString(465, y-l*lSpace, currencyFormater(value2['unitPrice']))
            totalUnitPrice =totalUnitPrice+int(value2['unitPrice'])
            invLine+=1
            l+=1

        l+=1
    #  
    can.setFont("Helvetica-Bold", 10)
    can.drawString(220, y-l*lSpace, 'TOTALS') 
    can.drawRightString(465, y-l*lSpace, currencyFormater(totalUnitPrice))
    can.drawRightString(525, y-l*lSpace, currencyFormater(totalSales))        
    can.drawRightString(580, y-l*lSpace, currencyFormater(totalPayment))
    l+=1

    
        

    can.drawString(20, y-l*lSpace, 'SALES CONTRIBUTIONS')
    l+=1

    can.setFont("Helvetica", 10)

    for (key, value) in printData['sellers'].items():
        if (y-(l+3)*lSpace<0):
            can.showPage()
            y=800
            l =0
            page+=1
            can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'SALES'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
            l+=1
            l+=1
        can.drawString(20, y-l*lSpace,key)     
        can.drawString(120, y-l*lSpace,  ': '+currencyFormater(value)) 
        l+=1



    can.showPage()
    y=800
    l =0
    page+=1
    
    


    can.setFont("Helvetica-Bold", 10)

    date = printData['date'] if ('date' in printData and printData['date']) else '--'

    can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'PURCHASE'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
    l+=1
    l+=1

    can.drawString(20, y-l*lSpace, 'INVOICE NO.')     
    can.drawString(120, y-l*lSpace, 'CUS DETAILS')     
    can.drawString(220, y-l*lSpace, 'ITEMS')        
    can.drawString(370, y-l*lSpace, 'WEIGHT')        
    can.drawString(420, y-l*lSpace, 'SOLD P')  
    can.drawString(490, y-l*lSpace, 'TOTAL') 

    can.drawString(535, y-l*lSpace, 'PAYMENT')        
    l+=1

    can.setFont("Helvetica", 10)
    totalSales=0
    totalPayment=0
    totalUnitPrice=0

    for (key, value) in  dict(sorted(printData['purchaseItems'].items())).items() :

        if (y-(l+4)*lSpace<0):
            can.showPage()
            y=800
            l =0
            page+=1
            can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'PURCHASE'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
            l+=1
            l+=1
            can.drawString(20, y-l*lSpace, 'INVOICE NO.')     
            can.drawString(120, y-l*lSpace, 'CUS DETAILS')     
            can.drawString(220, y-l*lSpace, 'ITEMS')        
            can.drawString(370, y-l*lSpace, 'WEIGHT')        
            can.drawString(420, y-l*lSpace, 'SOLD P')  
            can.drawString(490, y-l*lSpace, 'TOTAL') 

            can.drawString(535, y-l*lSpace, 'PAYMENT')        
            l+=1

        can.drawString(20, y-l*lSpace, value['invoiceSN'])     
        can.drawString(120, y-l*lSpace, value['name'])            
               
        can.drawRightString(525, y-l*lSpace, currencyFormater(value['total']))        
        can.drawRightString(580, y-l*lSpace, currencyFormater(value['payAmount']))  
        
        totalSales = value['total']+totalSales
        totalPayment = value['payAmount']+totalPayment

        
        invLine=1
        for (key2, value2) in  value['itemList'].items():
            # if (invLine==2):
            #     can.drawString(120, y-l*lSpace, value['namePhone'])
            if (y-(l+4)*lSpace<0):
                can.showPage()
                y=800
                l =0
                page+=1
                can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'PURCHASE'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                l+=1
                l+=1
                can.drawString(20, y-l*lSpace, 'INVOICE NO.')     
                can.drawString(120, y-l*lSpace, 'CUS DETAILS')     
                can.drawString(220, y-l*lSpace, 'ITEMS')        
                can.drawString(370, y-l*lSpace, 'WEIGHT')        
                can.drawString(420, y-l*lSpace, 'SOLD P')  
                can.drawString(490, y-l*lSpace, 'TOTAL') 

                can.drawString(535, y-l*lSpace, 'PAYMENT')        
                l+=1

            can.drawString(220, y-l*lSpace, (value2['label'][:30] + '..') if len(value2['label']) > 30 else value2['label'] )        
            can.drawRightString(410, y-l*lSpace, value2['weight']+'g')
            can.drawRightString(465, y-l*lSpace, currencyFormater(value2['unitPrice']))
            totalUnitPrice =totalUnitPrice+int(value2['unitPrice'])
            invLine+=1
            l+=1

        l+=1
    #  
    can.setFont("Helvetica-Bold", 10)
    can.drawString(220, y-l*lSpace, 'TOTALS') 
    can.drawRightString(465, y-l*lSpace, currencyFormater(totalUnitPrice))
    can.drawRightString(525, y-l*lSpace, currencyFormater(totalSales))        
    can.drawRightString(580, y-l*lSpace, currencyFormater(totalPayment))
    l+=1


    can.save()

    os.system('lp ./report.pdf')


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
 
