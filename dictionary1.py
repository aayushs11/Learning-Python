name_and_number = {
    'Aayush': '98XXXXXXXX',
    'Ram': '9810000000',
    'Krishna' : '9874563210'
}

print(type(name_and_number))

print(name_and_number['Aayush'])
print(name_and_number['Ram'])
print(name_and_number['Krishna'])

print('Aayush' in name_and_number)

for i in name_and_number:
    print(i)

print(f'key is {i} and value is {name_and_number[i]}')