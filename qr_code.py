from qrcode import make 

data = "https://raufjatoi.github.io/me/"
qr = make(data)
qr.save("rauf.png")