age = int(input("Whats your age:"))
country = input('Which counrtry you belongs to:')
status = 'Nepal'

if age>=18 and country==status:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')