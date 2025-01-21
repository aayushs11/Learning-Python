class animal():
    def __init__(self,name,size,color):  # Constructor method to initialize attributes
        self.name=name                   # Attribute: name of the animal
        self.size=size                   # Attribute: size of the animal
        self.color=color                 # Attribute: color of the animal
    
    def attribute(self):                 # Method to display the animal's attributes
        # If using `return`, this method would return the formatted string
        # return (f'The animals name is {self.name} size is {self.size} and colour is {self.color}')
    
        #Using print() to directly display the animal's attributes
        print (f'The animals name is {self.name} size is {self.size} and colour is {self.color}')

# Creating objects of the class `animal` with different attributes
a1=animal(size='huge',color='gray',name='Elephant')
a2=animal('Tiger','medium','orange')
a3=animal(name='Lion',size='medium',color='mixed')
a4=animal(name='Zebra',size='medium',color='white and black')

#when using return in method. This would print the returned string
# print(a1.attribute())
# print(a2.attribute())
# print(a3.attribute())
# print(a4.attribute())

#when using print in method. This directly prints the attributes without using an external print() function
a1.attribute()
a2.attribute()
a3.attribute()
a4.attribute()