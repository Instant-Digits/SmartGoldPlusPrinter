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

    can.drawString(70, 674, "Name")
    can.drawString(115, 674, ": "+printData['name'])

    can.drawString(255, 674, "Date")
    can.drawString(295, 674, ": "+printData['date'])


    can.drawString(440, 674, "Time")
    can.drawString(475, 674, ": "+printData['time'])

    can.drawString(70, 657, "Sample")
    can.drawString(115, 657, ": "+printData['sample'])


    can.drawString(255, 658, "Weight")
    can.drawString(295, 657, ": "+printData['weight']+'g')



    can.drawString(440, 657, "Karat")
    can.drawString(475, 657, ": "+printData['karad']+'K')


    can.setFont("Helvetica-Bold", 12)
    i=0
    for (key, value) in dict.items():
        y=590-i*20
        i=i+1
        can.drawString(80, y, "{:^12}".format( str(i)))
        can.drawString(140, y, key )#80
        
        can.drawString(445, y, printData[value]+'%')


    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("certificateTemp.pdf", "rb")) 
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("destination.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    return('destination.pdf')


#SetPrintingJobCertificate('')