class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.salary = salary
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        self.__salary = value
        if value < 0:
            self.__salary = 0
            print("Salary cannot be negative. Setting salary to 0.")
        else:
            print(f"Salary for {self.name} has been updated to {self.salary}")
            
    def promote(self, increase):
        self.increase = increase
        increase_amount = self.__salary * increase
        self.__salary += increase_amount
        print(f"{self.name} has been promoted. New salary: {self.salary}")
        

employee1 = Employee("Daniel", 500000)
employee2 = Employee("Sofía", 500000)
employee1.promote(0.10)
employee2.promote(0.10)