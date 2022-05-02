#Code by SecretBeast_bg01.
#Create your own Qrcode
import pyqrcode
import png 
from pyqrcode import QRCode



#string which represents the qr code 
s = "https://ishankhan01.000webhostapp.com/" 
#Generate qr code
url = pyqrcode.create(s)
#Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = s)
#Create and save thw svg file naming myqr.png
url.png ('myqr.png', scale=6)
