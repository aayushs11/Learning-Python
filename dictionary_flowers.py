#National Flowers of SAARC Countries
flowers= {
    'Nepal': 'Rhododendron',
    'India': 'Lotus',
    'Maldives': 'Rose',
    'Pakistan': 'Jasmine',
    'Afghanistan': 'Tulip',
    'Sri Lanka': 'Blue Lily',
    'Bhutan': 'Poppy',
    'Bangladesh': 'Water Lily'
}

print(type(flowers))
print(flowers)

#key-values of Nepal and Maldives
print(flowers['Nepal'])
print(flowers['Maldives'])

#changing the value of Nepal
flowers['Nepal']= 'Laliguras'
print(flowers['Nepal'])

#Adding new countries
flowers['Japan']= 'Sakura'
print(flowers)

flowers['France']= 'Iris'
print(flowers)

#Removing France from Dictionary
del flowers['France']
print(flowers)

#Loop to print keys
for flower in flowers.items():
    print(flower)

print()

#Loop to print keys with values
for flora in flowers.items():
    print(flora)