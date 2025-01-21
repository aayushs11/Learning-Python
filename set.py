city= {'Kathmandu','Lalitpur','Bhaktapur','Pokhara','Janakpur','Kathmandu'}

#check type and print
print(type(city))
print(city)

#adding new city
city.add('Biratnagar')
print(city)

#removing one city name from set
city.remove('Pokhara')
print(city)

#checking values in set
print('Kathmandu' in city)
for i in city:
    print(i)

#duplicate values is not displayed
check_duplicate= set(city)
print(city)