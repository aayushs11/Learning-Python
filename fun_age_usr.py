def year():
    current_year= int(input('Enter current year: '))
    date_of_birth= int(input('Enter your date of birth year: '))
    age= current_year-date_of_birth
    print(f'Your age is {age}')
year()