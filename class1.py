#Class
class laptop():
    def __init__(self,id,name,ram):
        self.id=id
        self.name=name
        self.ram=ram

    def get_details(self):
        return f'{self.id} {self.name} {self.ram}'
    
#Object
l1=laptop(id=1,name='Dell',ram='4GB')
l2=laptop(id=2,name='HP',ram='8GB')
l3=laptop(id=3,name='Acer',ram='16GB')


print(l1.get_details())
print(l2.get_details())
print(l3.get_details())