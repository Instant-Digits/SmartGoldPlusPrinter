import pyqrcode
import png
from PIL import Image, ImageDraw, ImageFont
import time

def setLabelPrinting(printer,  printingHeader,printData):     

    printer.align('center')
    printer.image(generateQRCode( printData['qr'],printData['karad'], [printingHeader['name'],'W: '+str(printData['weight'])+ 'g, ('+ floatToStr(float(printData['pPercentage'])+ float(printData['profitMargin'])-100)+')',
    printData['label'] 
   ]))
    printer.text('\x1dV\x00')
    #time.sleep(1)
    printer.lf()
    printer.lf()
    printer.text('\x1dV\x00')
    printer.lf()
    printer.lf()
    printer.lf()
   

def floatToStr(fl):
    k = int(fl)
    if (k==fl):
        return str(k)
    return str(fl)
   


def generateQRCode (code,karad, data):
    font = ImageFont.truetype('FreeSansBold.ttf', 10)   #/usr/share/fonts/truetype/freefont

    image = pyqrcode.create(code)
    image.png('qr.png', scale = 3.5, quiet_zone=0)

    qr_img = Image.open('qr.png', 'r')
    qr_img_w, qr_img_h = qr_img.size
    label = Image.new('RGBA', (600, qr_img_h+40), (255, 255, 255, 255))
    bg_w, bg_h = label.size


    offset = (40, (bg_h - qr_img_h) // 2)
    label.paste(qr_img, offset)

    d = ImageDraw.Draw(label)

    #d.text((10, qr_img_h+25), "SOFTWARED BY WWW.INSTANTDIGITS.COM",font=font, fill=(0, 0, 0))
    font = ImageFont.truetype('FreeSansBold.ttf', 20)
    d.text((245, qr_img_h/2+10), "X",font=font, fill=(0, 0, 0))

    font = ImageFont.truetype('FreeSansBold.ttf', 20)
    d.text((120, qr_img_h/2), "ID : "+code,font=font, fill=(0, 0, 0))
    d.text((145, qr_img_h/2+25), "("+str(karad)+'K)',font=font, fill=(0, 0, 0))

    
   
    font = ImageFont.truetype('FreeSansBold.ttf', 22)
    for i in range (0, len(data)):
        if (i==2):
            font = ImageFont.truetype('FreeSansBold.ttf', 20)
        elif(i>2):
            font = ImageFont.truetype('FreeSansBold.ttf', 18)

        d.text((340, (i+1)*30-20), data[i],font=font, fill=(0, 0, 0))
    

    #label.show()
    label.save('qr.png')
    return "./qr.png"


#generateQRCode ('123456',22, ['Shaganan', 'W: 12g S.P 101 %', 'Gold chain '])
