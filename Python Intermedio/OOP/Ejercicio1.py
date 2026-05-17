class Circle:
    radius = 25
    def get_area(self):
        area = 3.14 * self.radius ** 2
        print(f"The area is {area}")
        
my_area = Circle()

my_area.get_area()