height_in_cm = [145, 148, 150, 153, 158, 155, 160, 163, 170, 171, 175, 180]

# Displaying and counting small heights
print('Small heights:', small_height := [x for x in height_in_cm if x <= 150])
print('People with small height:', len(small_height))

# Displaying and counting average heights
print('Average heights:', average_height := [y for y in height_in_cm if y >= 160])
print('People with average height:', len(average_height))

# Displaying and counting tall heights
print('Tall heights:', tall_height := [z for z in height_in_cm if z >= 170])
print('People with tall height:', len(tall_height))