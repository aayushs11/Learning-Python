age= int(input('Enter your age: '))
if age<18:
    raise ValueError('Stay Back! You are just a kiddo')
else:
    print('You are too old')