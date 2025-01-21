#Duck Typing in Python
class dog:
    def speak(self):
        return 'Woof!'

class cat:
    def speak(self):
        return 'Meow!'
    
def make_animal_speak(animal):
        print(animal.speak())

dog= dog()
cat= cat()

make_animal_speak(dog)
make_animal_speak(cat)