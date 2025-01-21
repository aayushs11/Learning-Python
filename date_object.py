import datetime

#Date object
birth_date= datetime.date(1997,12,27)
print(f'My birthdate is on {birth_date}')

#Using strftime("%B") gives the full name of the month, and
#strftime("%b") gives the abbreviated month name (e.g., "Dec").
array= [birth_date.year,birth_date.strftime('%B'),birth_date.day]
print(f'My birth year is {array[0]}')
print(f'My birth month is {array[1]}')
print(f'My birth day is {array[2]}')

print(f'\nWish me on {array[1]} {array[2]}🎉🎂🥳')