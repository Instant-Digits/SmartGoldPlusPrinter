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

   

    can.drawString(70, 664, "Name")
    can.drawString(115, 664, ": "+printData['name'])

    can.drawString(255, 664, "Date")
    can.drawString(295, 664, ": "+printData['date'])


    can.drawString(440, 664, "Time")
    can.drawString(475, 664, ": "+printData['time'])

    can.drawString(70, 648, "Sample")
    can.drawString(115, 648, ": "+printData['sample'])


    can.drawString(255, 648, "Weight")
    can.drawString(295, 648, ": "+printData['weight']+'g')



    can.drawString(440, 648, "Karat")
    can.drawString(475, 648, ": "+printData['karad']+'K')


    can.setFont("Helvetica", 12)
    i=0
    for (key, value) in dict.items():
        y=580-i*20
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
    #os.system('lp ./destination.pdf')


#SetPrintingJobCertificate('')
