import qrcode 

data = 'King Luis Valladolid will be the BJJ GOAT and the BUSINESS MOGULE GOAT'

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/luism/OneDrive/Desktop/cs-projects/beginner-projects/6-quick-python-beginner-projects/qrcode/my_red_qrcode.png')


