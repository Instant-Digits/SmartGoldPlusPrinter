from escpos.connections import getUSBPrinter
import time
from textwrap import wrap
from escpos.connections import getUSBPrinter
import pyqrcode
import png
from PIL import Image, ImageDraw, ImageFont


printer = getUSBPrinter()(idVendor=0x1203,  # USB vendor and product Ids for Bixolon SRP-350plus
                        idProduct=0x0170,  # printer
                        inputEndPoint=0x82, #  lsusb -vvv -d 1203:0170 | grep bEndpointAddress | grep IN
                        outputEndPoint=0x01)

                        # (idVendor=0x0483,  # USB vendor and product Ids for Bixolon SRP-350plus
                        # idProduct=0x5743,  # printer
                        # inputEndPoint=0x82,
                        # outputEndPoint=0x01)



def generateQRCode (code, data):
    font = ImageFont.truetype('FreeSansBold.ttf', 10)   #/usr/share/fonts/truetype/freefont

    image = pyqrcode.create(code)
    image.png('qr.png', scale = 3.5, quiet_zone=0)

    qr_img = Image.open('qr.png', 'r')
    qr_img_w, qr_img_h = qr_img.size
    label = Image.new('RGBA', (512, qr_img_h+10), (255, 255, 255, 255))
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

        d.text((280, (i+1)*25-20), data[i],font=font, fill=(0, 0, 0))
    

    # label.show()
    label.save('qr.png')
    return "./qr.png"

printer.align('center')
printer.lf()
printer.image(generateQRCode ('000072', ['PRIYANKA JEWELS', 'W :10.3g, S.P 101%', 'Gold chain box']))
printer.lf()
printer.lf()
printer.image(generateQRCode ('000072', ['PRIYANKA JEWELS', 'W :10.3g, S.P 101%', 'Gold chain box']))

#printer.text("\0".encode())

# printer.feed(2)
# printer.image(generateQRCode ('000072', ['PRIYANKA JEWELS', 'W :10.3g, S.P 101%', 'Gold chain box']))
# printer.text('\x1dV\x00')
# printer.image(generateQRCode ('000072', ['PRIYANKA JEWELS', 'W :10.3g, S.P 101%', 'Gold chain box']))
# printer.text('\x1dV\x00')
# printer.image(generateQRCode ('000072', ['PRIYANKA JEWELS', 'W :10.3g, S.P 101%', 'Gold chain box']))
# printer.text('\x1dV\x00')

# printer.lf()
# printer.lf()
#printer.lf()

# printer.bold()
# printer.text('Priyanka JWELS')
# printer.lf()
# printer.text('13,4G')
# printer.lf()
# printer.text('Chain')
# printer.lf()

# printer.text('\x1dV\x00')
# time.sleep(1)
# printer.lf()
# printer.lf()
# printer.text('\x1dV\x00')
# printer.lf()
# printer.lf()
# #printer.lf()



