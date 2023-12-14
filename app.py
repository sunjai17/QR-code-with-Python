import pyqrcode
from pyqrcode import QRCode

# give a string?URL link  which tou want to represent the QRcode
URL= input("Enter your URL:")


#Generate the URL
QR=pyqrcode.create(URL)

#Create and save the png file naming my.png
QR.svg("my.png",scale=8)