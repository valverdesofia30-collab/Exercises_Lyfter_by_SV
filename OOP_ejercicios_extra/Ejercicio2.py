class Animal:
    def __init__ (self, name):
        self.name = name
    
    def speak(self):
        return "Make a sound"

class Dog(Animal):
    def speak(self):
        return "Guau"
    
class Cat(Animal):
    def speak(self):
        return "Miau"
    
dog = Dog("Rex")
print(dog.speak())

cat = Cat("Taco")
print(cat.speak())