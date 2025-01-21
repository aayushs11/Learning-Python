import qrcode

# Number of QR codes to generate
num_qr = int(input("How many QR codes do you want to generate? "))

for i in range(num_qr):
    print(f"Enter details for QR code {i+1}:")
    name = input('Name: ')
    address = input('Address: ')
    phone = input('Phone number: ')
    website = input('Website: ')
    
    # Combine the input data into a single string
    data = f"Name: {name}\nAddress: {address}\nPhone: {phone}\nWebsite: {website}"
    
    # Generate the QR code with combined data
    qr = qrcode.make(data)
    
    # Save the QR code image
    qr.save(f'{name}_QR.png')
    
    print(f'The QR code for {name} has been generated and saved as {name}_QR.png')

print('All QR codes have been generated and saved.')