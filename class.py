#Class
class student():
    def __init__(self,name,grade):
        self.name= name
        self.grade= grade
    
    def get_info(self):
        return f'Name is {self.name} and grade is {self.grade}'
    
    def is_passed(self):
        if self.grade>=60:
            return True
        else:
            return False

#Object
s1= student(name='Aayush',grade=55)
s2= student(name='Ram', grade=60)
s3= student(name='sita', grade=65)

print(s1.get_info())
print(s2.get_info())
print(s3.get_info())

print(s1.is_passed())
print(s2.is_passed())
print(s3.is_passed())