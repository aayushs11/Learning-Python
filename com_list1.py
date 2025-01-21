height_in_cm= [145,148,150,153,158,155,160,163,170,171,175,180]

print(height_in_cm)
cnt= print(len(height_in_cm))

#Displaying and counting small heights
small_height= [x for x in height_in_cm if x<=150]
print(small_height)
count=len(small_height)
print('People with small height are', count)

#Displaying and counting average heights
average_height=[y for y in height_in_cm if y>=160]
print('Averege height is', average_height)
count1= len(average_height)
print('People with average height are',count1)

#Displaying and counting tall heights
tall_height= [z for z in height_in_cm if z>=170]
print(tall_height)
count2= len(tall_height)
print('People with tall height are', count2)