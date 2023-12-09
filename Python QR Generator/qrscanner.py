import qrcode

qr = qrcode.QRCode()
qr.add_data("https://www.instagram.com/__always_nani?igshid=OGQ5ZDc2ODk2ZA==")
qr.make(fit=True)

qr_image = qr.make_image()
qr_image.save("qr_code.png")