#Parent class
class parent():
    def __init__(self,name,blood_group,eye_color):
        self.name= name
        self.blood_group= blood_group
        self.eye_color= eye_color

    def heridity(self):
        print(f"{self.name}'s blood group is {self.blood_group} and has {self.eye_color} eye color")

#Parent object
f1=parent('Aayush','B+','Brown')
f1.heridity()       

class child(parent):
    def __init__(self, name, blood_group, eye_color,son):
        super().__init__(name, blood_group, eye_color)
        self.son=son
        print(f"{self.name}'s son {self.son} has same blood group {self.blood_group} and eye color {self.eye_color} as of his father")
    
    def heridity(self):
        pass

#Object of child class inherits from parents
s1=child('Aayush','B+','Brown','Krishna')
s1.heridity()