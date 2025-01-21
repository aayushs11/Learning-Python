temp=int(input('Enter temperature degree in celcius: '))

if temp>=28:
    print('The weather is so hot.')
elif temp>=15 and temp<=28:
    print('The weather is normal')
else:
    print('The weather is cold')