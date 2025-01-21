#Base or parent class
class person():
    def __init__(self,name,age):
        self.name= name
        self.age=age
    
    def get_details(self):
        print(f'Person age is {self.name} and age is {self.age}')

#Derived or child class
class student(person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade= grade
    
    def get_details(self):
        super().get_details()
        print(f'The grade of {self.name} is {self.grade}')

#Object
s1= student(name='Aayush Shrestha',age=25,grade='75')
s1.get_details()