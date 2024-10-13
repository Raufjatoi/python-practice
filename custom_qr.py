import qrcode
from PIL import Image

# Data to be encoded
data = "https://raufjatoi.github.io/me/"

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create a colorful QR code with red fill and blue background
qr_img = qr.make_image(fill_color="red", back_color="blue")

# Save the final QR code
qr_img.save("red_blue_qr_code.png")
