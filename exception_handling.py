try:
    num1= float(input('Enter the first number: '))
    num2= float(input('Enter the second number: '))
    sum= num1+num2
    print(f'The sum of two numbers is {sum}')

except:
    print('Please enter valid number')
finally:
    print('Program Ends Here!')