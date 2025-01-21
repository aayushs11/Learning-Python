Person1= int(input('Enter Person 1 age:'))
Person2= int(input('Enter Person 2 age:'))

gap= Person1 - Person2

if Person1 == Person2:
    print('Same age')

if Person1>Person2:
    print(f'Person1 is elder that Person2')

if Person1<Person2:
    print(f'Person1 younger that Person2')