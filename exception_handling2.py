try:
    number= int(input('Enter any number: '))
    if number%2==0:
        print(f'{number} is even number.')
    else:
        print(f'{number} is odd number')

except ValueError:
    print('Please a number')