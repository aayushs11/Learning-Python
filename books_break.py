books = ['It ends with us','It starts with us', 'Ugly Love','November 9','Confess','This Girl']

for book in books:
    if book == 'Ugly Love':
        print(f'{book} book has been found')
        break
    print(f'Checking...\n{book}')   
print('Search Halted')