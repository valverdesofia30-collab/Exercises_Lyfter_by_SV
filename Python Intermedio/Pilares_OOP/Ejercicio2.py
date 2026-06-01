from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        print(f"The area of the circle is {area}")
        return area
        
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"The perimeter of the circle is {perimeter}")
        return perimeter

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        print(f"The area of the rectangle is {area}")
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        print(f"The perimeter of the rectangle is {perimeter}")
        return perimeter
    
    
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        area = self.side_length ** 2
        print(f"The area of the square is {area}")
        return area
        
    def calculate_perimeter(self):
        perimeter = 4 * self.side_length
        print(f"The perimeter of the square is {perimeter}")   
        return perimeter

circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(3)

circle.calculate_area()
circle.calculate_perimeter()

rectangle.calculate_area()
rectangle.calculate_perimeter()

square.calculate_area()
square.calculate_perimeter()