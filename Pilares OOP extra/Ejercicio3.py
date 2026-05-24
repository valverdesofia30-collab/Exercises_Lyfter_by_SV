class Vehicle:
    def __init__ (self, brand, year):
        self._brand = brand
        self._year = year
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        self._brand = value
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value
    
    def get_info(self):
        return (f"{self._brand}, {self._year}")
        
class Car(Vehicle):
    def __init__ (self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
        
    def get_info(self):
        base_info = super().get_info()
        final_info = f"{base_info}, {self.doors}"
        return final_info 
       
        
class Motorcycle(Vehicle):
    def __init__ (self, brand, year, motorcycle_type):
        super().__init__(brand, year)
        self.motorcycle_type = motorcycle_type
        
    def get_info(self):
        base_info = super().get_info()
        final_info = f"{base_info}, {self.motorcycle_type}"
        return final_info

vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Sport")

print(vehicle1.get_info())
print(vehicle2.get_info())