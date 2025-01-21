import datetime

birth_year= int(input('Enter your birth year: '))

#Get current year
today= datetime.date.today()
current_year= today.year
print(f'The current running year is {current_year}')

age= current_year - birth_year
print(f'Your age is {age}')