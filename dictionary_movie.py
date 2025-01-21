movie= {
    'The End of World': 2012,
    'The Earthquake': 2015,
    'Blockade in Nepal': 2015,
    'Burning Wildlife in AUS': 2019,
    'Corona Virus from China' : 2020,
    'Russia Vs Ukraine' : 2022,
    'Flood in Nepal': 2024,
    'Liyam Payne: The Legend': 2024
}
print(movie)

#Adding new movie
movie['One Direction Union in a Dream']= 2024
print(movie)

movie['Corona Virus from China']= 2019

#Removing the movie
movie.pop('Russia Vs Ukraine')
print(movie)

#Displaying key-value items
for real in movie:
    print(real)