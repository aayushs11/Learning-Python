#Creating contact details with dictionary
contact= {
    'Name':'Aayush Shrestha',
    'Phone': '9812345678',
    'Email': 'aayush.shrestha91@gmail.com',
    'Website': 'https://ajaayushblog.wordpress.com/'
}
print(contact)

#Accessing phone number
print(contact['Phone'])

#Updating Name
contact['Name']= 'AJ Aayush Shrestha'
print('Updatded Name:', contact )

#Adding new key-value
contact['Address']= 'Kathmandu, Nepal'
print(contact)

#Removing key-value
contact.pop('Address')
print(contact)