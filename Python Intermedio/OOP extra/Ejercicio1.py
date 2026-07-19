class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive numbers.")
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

try:
    rectangle = Rectangle (-10, 5)
    print(f"The area is {rectangle.get_area()}")
    print(f"The perimeter is {rectangle.get_perimeter()}")
except ValueError as i:
    print(f"Error: {i}")


