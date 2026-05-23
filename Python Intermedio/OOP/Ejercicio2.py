class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.persons = []
        
    def add_passenger(self, person):
       if len(self.persons) < self.max_passengers:
              self.persons.append(person)
              print(f"{person.name} has been added to the bus.")
       else:
                print("The bus is full. Cannot add more passengers.")

    def remove_passenger(self, person):
        if person in self.persons:
            self.persons.remove(person)
            print(f"{person.name} has been removed from the bus.")
        else:
            print(f"{person.name} is not on the bus.")

class Person:
    def __init__ (self, name):
        self.name = name

bus = Bus (5)
person1 = Person ("Alice")
person2 = Person ("Bob")
person3 = Person ("Charlie")
person4 = Person ("David")
person5 = Person ("Eve")


bus.add_passenger(person1)
bus.add_passenger(person2)
bus.add_passenger(person3)
bus.add_passenger(person4)
bus.add_passenger(person5)