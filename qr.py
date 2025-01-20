from qrcode import QRCode

def qrcode(data):
    qr = QRCode()
    qr.add_data(data)
    img = qr.make_image()
    return img
data = "ENTER TEXT OR URL HERE"
qr_code = qrcode(data)
print("QR-code:", data)
qr_code.save("qr_code_example.png")