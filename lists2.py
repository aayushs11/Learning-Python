god = []

god.append('Aayush')
god.append('Mitra')
god.append('Agni')
god.append('Indra')
god.append('Ajaekpada')
god.append('Varuna')
god.append('Ahirbudnya')

# Finding names that start with the letter 'A'
names_starting_with_a = [name for name in god if name.lower().startswith('a')]
print("Names starting with 'A':", names_starting_with_a)

# Finding names that do NOT start with the letter 'A'
remaining_names = [name for name in god if not name.lower().startswith('a')]
print("Names not starting with 'A':", remaining_names)