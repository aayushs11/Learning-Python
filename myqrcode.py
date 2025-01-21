import qrcode

name= input('Name: ')
img= qrcode.make(name)

print(type(img))
img.save(f'{name}.png')

print('QR saved sucessfully')