# No Parameter No And No Return Type
def function():
    print('Welcome to my World')
function()

#Parameter And No Return Type
def diff(num1,num2):
    value= num1-num2
    print(f'The differences is {value}')
diff(11,3)

#No Parameter And Return Type
def age():
    return 18
fn= int(input('ENter your age to check your voter eligibility: '))
if fn>=18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

#Parameter And Return Type
def full_name(first_name, last_name):
    fullname= (f'{first_name} {last_name}')
    return fullname

fn=full_name('Aayush','Shrestha')
print(fn)