import qrcode

qr = qrcode.QRCode(
    version= 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size= 9,
    border= 2,
)

# Link que queremos mostrar
qr.add_data("https://www.linkedin.com/in/hernan-rosero/")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr.png")
