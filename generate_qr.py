# generate_qr.py
import qrcode

# Data to encode in the QR Code
data = "https://github.com/Sandeep271/QRCode-Generator"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

# Generate image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qrcode.png")

print("QR code generated and saved as 'my_qrcode.png'")
