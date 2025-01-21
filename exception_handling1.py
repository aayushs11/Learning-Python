try:
    number= int(input('Enter any number:'))
    result= 113/number
    print(result)

except ValueError:
    print('Error: Please enter a number')

except ZeroDivisionError:
    print('Error: Number cannot be divisible by ZERO! ')