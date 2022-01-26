import pyqrcode
import png
from PIL import Image, ImageDraw, ImageFont
import time

def setLabelPrinting(printer,  printingHeader,printData):     

    printer.align('center')
    printer.image(generateQRCode( printData['qr'], [printingHeader['name'],'W : '+str(printData['weight'])+ 'g,  S.P %'+ str(int(printData['pPercentage'])+ int(printData['profitMargin'])),
    " ".join(printData['id'].split('_')[ 0: len(printData['id'].split('_'))-1]) 
   ]))
    printer.text('\x1dV\x00')
    time.sleep(1)
    printer.lf()
    printer.lf()
    printer.text('\x1dV\x00')
    printer.lf()
    printer.lf()
    printer.lf()
   


def generateQRCode (code, data):
    font = ImageFont.truetype('FreeSansBold.ttf', 10)   #/usr/share/fonts/truetype/freefont

    image = pyqrcode.create(code)
    image.png('qr.png', scale = 3.5, quiet_zone=0)

    qr_img = Image.open('qr.png', 'r')
    qr_img_w, qr_img_h = qr_img.size
    label = Image.new('RGBA', (512, qr_img_h+40), (255, 255, 255, 255))
    bg_w, bg_h = label.size


    offset = (0, (bg_h - qr_img_h) // 2)
    label.paste(qr_img, offset)

    d = ImageDraw.Draw(label)

    #d.text((10, qr_img_h+25), "SOFTWARED BY WWW.INSTANTDIGITS.COM",font=font, fill=(0, 0, 0))
    

    font = ImageFont.truetype('FreeSansBold.ttf', 20)
    d.text((90, qr_img_h/2+5), "ID : "+code,font=font, fill=(0, 0, 0))
   
    font = ImageFont.truetype('FreeSansBold.ttf', 22)
    for i in range (0, len(data)):
        if (i==2):
            font = ImageFont.truetype('FreeSansBold.ttf', 20)
        elif(i>2):
            font = ImageFont.truetype('FreeSansBold.ttf', 18)

        d.text((280, (i+1)*30-20), data[i],font=font, fill=(0, 0, 0))
    

    #label.show()
    label.save('qr.png')
    return "./qr.png"
