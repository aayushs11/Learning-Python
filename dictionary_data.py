data= {
    'Nepal' : 'Kathmandu',
    'India' : 'New Delhi'
}

print(type(data))
print(data.items())
print(data)

#Displaying Nepal data
print(data['Nepal'])

#Replacing the value of Nepal
data['Nepal']= 'KTM'
print(data)

#Adding new country
data['UK']= 'London'
print(data)

#Removing key-value
data.pop('India')
print(data)