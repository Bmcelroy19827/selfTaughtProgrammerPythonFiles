# 1
class Apple():
    def __init__(self, size, weight, color, age):
        self.size = size
        self.weight = weight
        self.color = color
        self.age = age

    def print_info(self):
        print("Size: {}\nWeight: {}\nColor: {}\nAge: {}".format(self.size, self.weight, self.color, self.age))

new_apple = Apple(10, 12, "Red", 30)
new_apple.print_info()

# 2
import math
class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
    def area(self):
        self.area = math.pi * math.pow(self.radius, 2)
        print(self.area)

first_circle = Circle(10)
first_circle.area()

# 3
class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base * self.height)/2

first_triangle = Triangle(4, 2)
print(first_triangle.area())

# 4
class RegularHexagon():
    def __init__(self, side):
        self.side  = side
    def perimeter(self):
        return self.side * 6

equi_hexigon = RegularHexagon(5)
print(equi_hexigon.perimeter())
