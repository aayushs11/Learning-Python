#Parent class
class vehicle():
    def __init__(self,color,model):
        self.colors=color
        self.models=model
    
    def properities(self):
        print(f'The vehicle color is {self.colors} and model is {self.models}')

#Parent's class object   
v1=vehicle('Black','Cadillac')
v1.properities()

#Child class inherits from vehicle
class car(vehicle):
    def __init__(self, color, model,year):
        super().__init__(color, model)
        self.years=year
    
    def properities(self):
        print(f'The car model is {self.models} in {self.colors} released in {self.years}')
             
#Child class Objects
c1= car('Black','Cadillac','2012')
c2= car('White','Ford','1999')
c3= car('Silver','Volkswagen','2003')
c4= car('Red','Audi','2001')
c1.properities()
c2.properities()
c3.properities()
c4.properities()