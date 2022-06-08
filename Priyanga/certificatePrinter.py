from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from functions import currencyFormater
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


dict ={
    "Gold (Au)":'Au', 
    "Copper (Cu)":'Cu',
    "Silver (Ag)":'Ag',
    "Indium (In)":'In',
    "Zinc (Zn)":'Zn'
}


def SetPrintingJobCertificate(printData):

    global dict

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    can.setFont("Helvetica-Bold", 11)
    top =657
    l=0
    lSpace=17

    can.drawString(60, top-l*lSpace, "Name")
    can.drawString(105,  top-l*lSpace, ": "+printData['name'])

    can.drawString(245,  top-l*lSpace, "Date")
    can.drawString(285,  top-l*lSpace, ": "+printData['date'])

    l+=1

    can.drawString(60,  top-l*lSpace, "Sample")
    can.drawString(105,  top-l*lSpace, ": "+printData['sample'])


    can.drawString(245,  top-l*lSpace, "Time")
    can.drawString(285,  top-l*lSpace, ": "+printData['time'])

    l+=1


    can.drawString(60,  top-l*lSpace, "Weight")
    can.drawString(105,  top-l*lSpace, ": "+printData['weight']+'g')



    can.drawString(245,  top-l*lSpace, "Karat")
    can.drawString(285,  top-l*lSpace, ": "+printData['karad']+'K')


    can.setFont("Helvetica", 11)
    i=0
    for (key, value) in dict.items():
        y=585-i*17
        i=i+1
        # can.drawString(80, y, "{:^12}".format( str(i)))
        can.drawString(60, y, key )#80
        
        can.drawString(280, y, printData[value]+'%')


    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("priyankaCert.pdf", "rb")) 
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


#SetPrintingJobCertificate('')