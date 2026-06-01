class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = 3.14 * self.radius ** 2
        return area


my_area = Circle(25)

print(f"The area is {my_area.get_area()}")