from pyzbar.pyzbar import decode
from PIL import Image


img = Image.open('C:/Users/luism/OneDrive/Desktop/cs-projects/beginner-projects/6-quick-python-beginner-projects/qrcode/my_red_qrcode.png')
result = decode(img)

print(result)