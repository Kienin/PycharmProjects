import qrcode
img = qrcode.make("https://www.longhornsteakhouse.com/home")
img.save("qr.png", "PNG")
