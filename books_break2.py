books = ['Slammed', 'Point of Retreat', 'This Girl', 'Hopeless', 'Losing Hope', 'Finding Cinderella', 'Maybe Someday',
        'Ugly Love', 'Confess', 'November 9', 'It Ends with Us', 'Without Merit', 'All Your Perfects', 'Verity',
        'Regretting You', 'Heart Bones', ' Layla', 'Reminders of Him', 'It Starts with Us', 'Too Late']

user_input= input('Enter any Book Name: ')

for book in books:
    if book.lower() == user_input.lower():
        print(f'{user_input} book has been found')
        break
    print(f'Checking for...\n{user_input}')   
else:
    print(f'{user_input} Book NOT FOUND')
print('Search Halted')
