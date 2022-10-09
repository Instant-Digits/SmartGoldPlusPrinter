import os
from functions import currencyFormater,nameDecode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from collections import OrderedDict


def SetPrintingJobReport(printData):

 
    pdf_file = 'destination.pdf'
 
    can = canvas.Canvas(pdf_file)

    itemsKaradW={}
    itemsKaradUP={}

    userInvoiceCount={}
    
    R1=20
    R2=100
    R3=200
    R4=360

    y=800
    l =0
    lSpace=14
    page =1
    if ('salesItems' in printData and len(printData['salesItems'])>0):    

    
        can.setFont("Helvetica-Bold", 10)

        date = printData['date'] if ('date' in printData and printData['date']) else '--'

        can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'SALES'+'    DATE : '+date+ "      Printed on : "+printData['printedOn'])#+ printData['printedOn']
        l+=1
        l+=1

        can.drawString(R1, y-l*lSpace, 'INVOICE NO.')     
        can.drawString(R2, y-l*lSpace, 'CUS DETAILS')     
        can.drawString(R3, y-l*lSpace, 'ITEMS')        
        can.drawString(R4, y-l*lSpace, 'WEIGHT')        
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
                can.drawString(R1, y-l*lSpace, 'INVOICE NO.')     
                can.drawString(R2, y-l*lSpace, 'CUS DETAILS')     
                can.drawString(R3, y-l*lSpace, 'ITEMS')        
                can.drawString(R4, y-l*lSpace, 'WEIGHT')        
                can.drawString(420, y-l*lSpace, 'SOLD P')  
                can.drawString(490, y-l*lSpace, 'TOTAL') 

                can.drawString(535, y-l*lSpace, 'PAYMENT')        
                l+=1

            can.drawString(R1, y-l*lSpace, value['invoiceSN'])     
            can.drawString(R2, y-l*lSpace, value['name'])            
                
            can.drawRightString(525, y-l*lSpace, currencyFormater(value['total']))        
            can.drawRightString(580, y-l*lSpace, currencyFormater(value['payAmount']))  
            
            totalSales = value['total']+totalSales
            totalPayment = value['payAmount']+totalPayment

            
            invLine=1
            for (key2, value2) in  value['itemList'].items():
                # if (invLine==2):
                #     can.drawString(R2, y-l*lSpace, value['namePhone'])
                if (y-(l+4)*lSpace<0):
                    can.showPage()
                    y=800
                    l =0
                    page+=1
                    can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'SALES'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                    l+=1
                    l+=1
                    can.drawString(R1, y-l*lSpace, 'INVOICE NO.')     
                    can.drawString(R2, y-l*lSpace, 'CUS DETAILS')     
                    can.drawString(R3, y-l*lSpace, 'ITEMS')        
                    can.drawString(R4, y-l*lSpace, 'WEIGHT')        
                    can.drawString(420, y-l*lSpace, 'SOLD P')  
                    can.drawString(490, y-l*lSpace, 'TOTAL') 

                    can.drawString(535, y-l*lSpace, 'PAYMENT')        
                    l+=1

                can.drawString(R3, y-l*lSpace, (value2['label'][:30] + '..') if len(value2['label']) > 30 else value2['label'] )        
                can.drawRightString(400, y-l*lSpace, value2['weight']+'g')
                can.drawRightString(465, y-l*lSpace, currencyFormater(value2['unitPrice']))
                totalUnitPrice =totalUnitPrice+int(value2['unitPrice'])
                invLine+=1
                l+=1

                if ('karad' in value2 and value2['karad'] ):
                    # value2['weight']=value2['weight'].replace('-', '.')
                    try :
                        value2['weight']=float(value2['weight'])
                    except :
                        value2['weight']=0
                    
                    itemsKaradW[value2['karad']]=(itemsKaradW[value2['karad']] if value2['karad'] in itemsKaradW else 0 )+float(value2['weight'])
                    itemsKaradUP[value2['karad']]=(itemsKaradUP[value2['karad']] if value2['karad'] in itemsKaradUP else 0 )+int(value2['unitPrice'])
                
            userInvoiceCount[value['issuedby']]=(userInvoiceCount[value['issuedby']] if value['issuedby'] in userInvoiceCount else 0 )+1


            l+=1
        #  
        can.setFont("Helvetica-Bold", 10)
        can.drawString(R3, y-l*lSpace, 'TOTALS') 
        can.drawRightString(465, y-l*lSpace, currencyFormater(totalUnitPrice))
        can.drawRightString(525, y-l*lSpace, currencyFormater(totalSales))        
        can.drawRightString(580, y-l*lSpace, currencyFormater(totalPayment))
        l+=1
        l+=1

        
            

        columnBreak = l

        can.drawString(R1, y-l*lSpace, 'SALES CONTRIBUTIONS')
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
            can.drawString(R1, y-l*lSpace,key)
            can.drawString(R2+20, y-l*lSpace,  ': '+currencyFormater(userInvoiceCount[key])+' Invs') 
            can.drawString(180, y-l*lSpace,  ': Rs. '+currencyFormater(value)) 
            l+=1

        l = columnBreak
        can.setFont("Helvetica-Bold", 10)
        can.drawString(340, y-l*lSpace, 'SALES DETAILS BY KARAT')
        l+=1

        can.drawString(350, y-l*lSpace,'KARAT')     
        can.drawString(400, y-l*lSpace,  'WEIGHT(g)' ) 
        can.drawString(480, y-l*lSpace,  'AMOUNT') 
        l+=1

        can.setFont("Helvetica", 10)

        for (key, value) in itemsKaradW.items():
            if (y-(l+3)*lSpace<0):
                can.showPage()
                y=800
                l =0
                page+=1
                can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'SALES'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                l+=1
                l+=1
            can.drawString(350, y-l*lSpace,key)     
            can.drawString(400, y-l*lSpace,  currencyFormater(value)+'g') 
            can.drawString(480, y-l*lSpace,  'Rs. '+currencyFormater(itemsKaradUP[key])) 
            l+=1



    if ( 'purchaseItems' in printData and len(printData['purchaseItems'])>0): 
        
        can.showPage()
        y=800
        l =0
        page+=1
        
        itemsKaradW={}
        itemsKaradUP={}

        userInvoiceCount={}
        userInvoiceAmount={}



        can.setFont("Helvetica-Bold", 10)

        date = printData['date'] if ('date' in printData and printData['date']) else '--'

        

        can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'PURCHASE'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
        l+=1
        l+=1

        can.drawString(R1, y-l*lSpace, 'INVOICE NO.')     
        can.drawString(R2, y-l*lSpace, 'CUS DETAILS')     
        can.drawString(R3, y-l*lSpace, 'ITEMS')        
        can.drawString(R4, y-l*lSpace, 'WEIGHT')        
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
                can.drawString(R1, y-l*lSpace, 'INVOICE NO.')     
                can.drawString(R2, y-l*lSpace, 'CUS DETAILS')     
                can.drawString(R3, y-l*lSpace, 'ITEMS')        
                can.drawString(R4, y-l*lSpace, 'WEIGHT')        
                can.drawString(420, y-l*lSpace, 'SOLD P')  
                can.drawString(490, y-l*lSpace, 'TOTAL') 

                can.drawString(535, y-l*lSpace, 'PAYMENT')        
                l+=1

            can.drawString(R1, y-l*lSpace, value['invoiceSN'])     
            can.drawString(R2, y-l*lSpace, value['name'])            
                
            can.drawRightString(525, y-l*lSpace, currencyFormater(value['total']))        
            can.drawRightString(580, y-l*lSpace, currencyFormater(value['payAmount']))  
            
            totalSales = value['total']+totalSales
            totalPayment = value['payAmount']+totalPayment

            
            invLine=1
            for (key2, value2) in  value['itemList'].items():
                # if (invLine==2):
                #     can.drawString(R2, y-l*lSpace, value['namePhone'])
                if (y-(l+4)*lSpace<0):
                    can.showPage()
                    y=800
                    l =0
                    page+=1
                    can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'PURCHASE'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                    l+=1
                    l+=1
                    can.drawString(R1, y-l*lSpace, 'INVOICE NO.')     
                    can.drawString(R2, y-l*lSpace, 'CUS DETAILS')     
                    can.drawString(R3, y-l*lSpace, 'ITEMS')        
                    can.drawString(R4, y-l*lSpace, 'WEIGHT')        
                    can.drawString(420, y-l*lSpace, 'SOLD P')  
                    can.drawString(490, y-l*lSpace, 'TOTAL') 

                    can.drawString(535, y-l*lSpace, 'PAYMENT')        
                    l+=1
                try :
                    printWeight = ('K'+value2['karad']+'| '+'A'+value2['actWeight']+'| '+ value2['weight']) if ('actWeight' in value2  ) else value2['weight']
                except :
                    printWeight='0.000'
                can.setFont("Helvetica", 8)   
                can.drawString(R3, y-l*lSpace, (value2['label'][:28] + '..') if len(value2['label']) > 28 else value2['label'] )        
                             
                can.drawRightString(415, y-l*lSpace,printWeight )
                can.setFont("Helvetica", 10)
                can.drawRightString(465, y-l*lSpace, currencyFormater(value2['unitPrice']))
                totalUnitPrice =totalUnitPrice+int(value2['unitPrice'])
                invLine+=1
                l+=1
                if ('karad' in value2 and value2['karad'] ):
                    itemsKaradW[value2['karad']]=(itemsKaradW[value2['karad']] if value2['karad'] in itemsKaradW else 0 )+float(value2['weight'])
                    itemsKaradUP[value2['karad']]=(itemsKaradUP[value2['karad']] if value2['karad'] in itemsKaradUP else 0 )+int(value2['unitPrice'])
                
            userInvoiceCount[value['issuedby']]=(userInvoiceCount[value['issuedby']] if value['issuedby'] in userInvoiceCount else 0 )+1
            userInvoiceAmount[value['issuedby']]=(userInvoiceAmount[value['issuedby']] if value['issuedby'] in userInvoiceAmount else 0 )+value['total']

            l+=1
        #  
        can.setFont("Helvetica-Bold", 10)
        can.drawString(R3, y-l*lSpace, 'TOTALS') 
        can.drawRightString(465, y-l*lSpace, currencyFormater(totalUnitPrice))
        can.drawRightString(525, y-l*lSpace, currencyFormater(totalSales))        
        can.drawRightString(580, y-l*lSpace, currencyFormater(totalPayment))
        l+=1
        l+=1

        columnBreak = l

        can.drawString(R1, y-l*lSpace, 'PURCHASE CONTRIBUTIONS')
        l+=1    

        can.setFont("Helvetica", 10)

        for (key, value) in userInvoiceAmount.items():
            if (y-(l+3)*lSpace<0):
                can.showPage()
                y=800
                l =0
                page+=1
                can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'SALES'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                l+=1
                l+=1
            can.drawString(R1, y-l*lSpace,key)
            can.drawString(R2, y-l*lSpace,  ': '+currencyFormater(userInvoiceCount[key])+' Invs') 
            can.drawString(180, y-l*lSpace,  ': Rs. '+currencyFormater(value)) 
            l+=1

        l = columnBreak

        can.setFont("Helvetica-Bold", 10)
        can.drawString(340, y-l*lSpace, 'PURCHASE DETAILS BY KARAT')
        l+=1

        can.drawString(350, y-l*lSpace,'KARAT')     
        can.drawString(400, y-l*lSpace,  'WEIGHT(g)' ) 
        can.drawString(480, y-l*lSpace,  'AMOUNT') 
        l+=1
        

        can.setFont("Helvetica", 10)

        for (key, value) in itemsKaradW.items():
            if (y-(l+3)*lSpace<0):
                can.showPage()
                y=800
                l =0
                page+=1
                can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'PURCHASE'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                l+=1
                l+=1
            can.drawString(350, y-l*lSpace,key)     
            can.drawString(400, y-l*lSpace,  currencyFormater(value)+'g' if (value>0) else 'N.A') 
            can.drawString(480, y-l*lSpace,  'Rs. '+currencyFormater(itemsKaradUP[key])) 
            l+=1

    if ( 'orderItems' in printData and len(printData['orderItems'])>0): 
        
        can.showPage()
        y=800
        l =0
        page+=1
        
        itemsKaradW={}
        itemsKaradUP={}

        userInvoiceCount={}
        userInvoiceAmount={}



        can.setFont("Helvetica-Bold", 10)

        date = printData['date'] if ('date' in printData and printData['date']) else '--'

        

        can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'ORDER'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
        l+=1
        l+=1

        can.drawString(R1, y-l*lSpace, 'INVOICE NO.')     
        can.drawString(R2, y-l*lSpace, 'CUS DETAILS')     
        can.drawString(R3, y-l*lSpace, 'ITEMS')        
        can.drawString(R4, y-l*lSpace, 'WEIGHT')        
        can.drawString(420, y-l*lSpace, 'SOLD P')  
        can.drawString(490, y-l*lSpace, 'TOTAL') 

        can.drawString(535, y-l*lSpace, 'PAYMENT')        
        l+=1

        can.setFont("Helvetica", 10)
        totalSales=0
        totalPayment=0
        totalUnitPrice=0

        for (key, value) in  dict(sorted(printData['orderItems'].items())).items() :

            if (y-(l+4)*lSpace<0):
                can.showPage()
                y=800
                l =0
                page+=1
                can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'ORDER'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                l+=1
                l+=1
                can.drawString(R1, y-l*lSpace, 'INVOICE NO.')     
                can.drawString(R2, y-l*lSpace, 'CUS DETAILS')     
                can.drawString(R3, y-l*lSpace, 'ITEMS')        
                can.drawString(R4, y-l*lSpace, 'WEIGHT')        
                can.drawString(420, y-l*lSpace, 'SOLD P')  
                can.drawString(490, y-l*lSpace, 'TOTAL') 

                can.drawString(535, y-l*lSpace, 'PAYMENT')        
                l+=1

            can.drawString(R1, y-l*lSpace, value['invoiceSN'])     
            can.drawString(R2, y-l*lSpace, value['name'])            
                
            can.drawRightString(525, y-l*lSpace, currencyFormater(value['total']))        
            can.drawRightString(580, y-l*lSpace, currencyFormater(value['payAmount']))  
            
            totalSales = value['total']+totalSales
            totalPayment = value['payAmount']+totalPayment

            
            invLine=1
            for (key2, value2) in  value['itemList'].items():
                # if (invLine==2):
                #     can.drawString(R2, y-l*lSpace, value['namePhone'])
                if (y-(l+4)*lSpace<0):
                    can.showPage()
                    y=800
                    l =0
                    page+=1
                    can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'ORDER'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                    l+=1
                    l+=1
                    can.drawString(R1, y-l*lSpace, 'INVOICE NO.')     
                    can.drawString(R2, y-l*lSpace, 'CUS DETAILS')     
                    can.drawString(R3, y-l*lSpace, 'ITEMS')        
                    can.drawString(R4, y-l*lSpace, 'WEIGHT')        
                    can.drawString(420, y-l*lSpace, 'SOLD P')  
                    can.drawString(490, y-l*lSpace, 'TOTAL') 

                    can.drawString(535, y-l*lSpace, 'PAYMENT')        
                    l+=1

                can.drawString(R3, y-l*lSpace, (value2['label'][:30] + '..') if len(value2['label']) > 30 else value2['label'] )        
                can.drawRightString(400, y-l*lSpace, value2['weight']+'g')
                can.drawRightString(465, y-l*lSpace, currencyFormater(value2['unitPrice']))
                totalUnitPrice =totalUnitPrice+int(value2['unitPrice'])
                invLine+=1
                l+=1
                if ('karad' in value2 and value2['karad'] ):
                    itemsKaradW[value2['karad']]=(itemsKaradW[value2['karad']] if value2['karad'] in itemsKaradW else 0 )+float(value2['weight'])
                    itemsKaradUP[value2['karad']]=(itemsKaradUP[value2['karad']] if value2['karad'] in itemsKaradUP else 0 )+int(value2['unitPrice'])
                
            userInvoiceCount[value['issuedby']]=(userInvoiceCount[value['issuedby']] if value['issuedby'] in userInvoiceCount else 0 )+1
            userInvoiceAmount[value['issuedby']]=(userInvoiceAmount[value['issuedby']] if value['issuedby'] in userInvoiceAmount else 0 )+value['total']

            l+=1
        #  
        can.setFont("Helvetica-Bold", 10)
        can.drawString(R3, y-l*lSpace, 'TOTALS') 
        can.drawRightString(465, y-l*lSpace, currencyFormater(totalUnitPrice))
        can.drawRightString(525, y-l*lSpace, currencyFormater(totalSales))        
        can.drawRightString(580, y-l*lSpace, currencyFormater(totalPayment))
        l+=1
        l+=1

        columnBreak = l

        can.drawString(R1, y-l*lSpace, 'ORDER CONTRIBUTIONS')
        l+=1    

        can.setFont("Helvetica", 10)

        for (key, value) in userInvoiceAmount.items():
            if (y-(l+3)*lSpace<0):
                can.showPage()
                y=800
                l =0
                page+=1
                can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'SALES'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                l+=1
                l+=1
            can.drawString(R1, y-l*lSpace,key)
            can.drawString(R2, y-l*lSpace,  ': '+currencyFormater(userInvoiceCount[key])+' Invs') 
            can.drawString(180, y-l*lSpace,  ': Rs. '+currencyFormater(value)) 
            l+=1

        l = columnBreak

        can.setFont("Helvetica-Bold", 10)
        can.drawString(340, y-l*lSpace, 'ORDER DETAILS BY KARAT')
        l+=1

        can.drawString(350, y-l*lSpace,'KARAT')     
        can.drawString(400, y-l*lSpace,  'WEIGHT(g)' ) 
        can.drawString(480, y-l*lSpace,  'AMOUNT') 
        l+=1
        

        can.setFont("Helvetica", 10)

        for (key, value) in itemsKaradW.items():
            if (y-(l+3)*lSpace<0):
                can.showPage()
                y=800
                l =0
                page+=1
                can.drawString(40, y-l*lSpace,'PAGE NO : '+str(page)+'    CODE : '+'firmCode'+'    TYPE : '+'ORDER'+'    DATE : '+date+ "      Printed on : "+ printData['printedOn'])
                l+=1
                l+=1
            can.drawString(350, y-l*lSpace,key)     
            can.drawString(400, y-l*lSpace,  currencyFormater(value)+'g') 
            can.drawString(480, y-l*lSpace,  'Rs. '+currencyFormater(itemsKaradUP[key])) 
            l+=1


    can.save()

    return 'destination.pdf'


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
 
