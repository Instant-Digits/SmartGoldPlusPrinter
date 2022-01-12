from textwrap import wrap
from escpos.connections import getUSBPrinter
import pyqrcode
import png
from PIL import Image, ImageDraw, ImageFont

from pyqrcode import QRCode

def currencyFormater (num):
    desimalIndex= str(num).find('.')
    if desimalIndex>-1:
        list = wrap(str(num)[desimalIndex-1::-1], 3)
        return ','.join(list)[::-1]+str(num)[desimalIndex:desimalIndex+3] 
    list = wrap(str(num)[::-1], 3)
    return ','.join(list)[::-1]

def configPrinters (configData):
    printers={}
    if ('config' in configData.keys()):
        printerConfig =configData['config']
        for (key, value) in printerConfig.items():
            try:
                printers[key] = getUSBPrinter()(idVendor=int(value['idVendor'],16),  # USB vendor and product Ids for Bixolon SRP-350plus
                                                idProduct=int(value['idProduct'],16),  # printer
                                                inputEndPoint=int(value['inputEndPoint'],16),
                                                outputEndPoint=int(value['outputEndPoint'],16))
                print (key+' DETECTED')
            except RuntimeError:
                print (key+' NOT DETECTED')
                return False
        return printers
    return (False)


def generateQRCode (code, data):
    font = ImageFont.truetype('FreeSansBold.ttf', 10)   #/usr/share/fonts/truetype/freefont

    image = pyqrcode.create(code)
    image.png('qr.png', scale = 6, quiet_zone=0)

    qr_img = Image.open('qr.png', 'r')
    qr_img_w, qr_img_h = qr_img.size
    label = Image.new('RGBA', (512, qr_img_h+40), (255, 255, 255, 255))
    bg_w, bg_h = label.size


    offset = (0, (bg_h - qr_img_h) // 2)
    label.paste(qr_img, offset)

    d = ImageDraw.Draw(label)

    d.text((10, qr_img_h+25), "SOFTWARED BY WWW.INSTANTDIGITS.COM",font=font, fill=(0, 0, 0))
    

    font = ImageFont.truetype('FreeSansBold.ttf', 18)
    d.text((135, qr_img_h/2+5), "ID : "+code,font=font, fill=(0, 0, 0))
   
    font = ImageFont.truetype('FreeSansBold.ttf', 25)
    for i in range (0, len(data)):
        if (i==2):
            font = ImageFont.truetype('FreeSansBold.ttf', 22)
        elif(i>2):
            font = ImageFont.truetype('FreeSansBold.ttf', 20)

        d.text((280, (i+1)*30-10), data[i],font=font, fill=(0, 0, 0))
    

    # label.show()
    label.save('qr.png')
    return "./qr.png"





#print (currencyFormater('12345.50000'))