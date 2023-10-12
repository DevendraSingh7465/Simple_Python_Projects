import pyqrcode , os

directory = os.getcwd()

s = "devendrasingh"
create_qr = pyqrcode.create(s)
create_qr.show()
create_qr.png('qrcode.png', scale=8)
print('QR Code Created at',directory)

