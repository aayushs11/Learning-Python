laptop= ['Dell','Acer','Lenovo','Toshiba','HP']

print(laptop)
print(len(laptop))

length =len(laptop)
print(length)

print(laptop[0])
print(laptop[-1])
print(laptop[-2])

laptop.append('Asus')
print(laptop)

laptop.remove('Lenovo')
print(laptop)

# This wont works
# laptop.remove([0])
# print(laptop)

del laptop[0]
print(laptop)

laptop.reverse()
print(laptop)