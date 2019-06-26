#Challenges

class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, l, w):
        self.len = l
        self.width = w
    def calculate_perimeter(self):
        return 2*self.len + 2*self.width

class Square(Rectangle):
    def __init__(self,l):
        self.len = l
        self.width = l

    def change_size(self, number):
        self.len += number
        self.width += number

first_rectangle = Rectangle(10,2)
print(first_rectangle.calculate_perimeter())
first_square = Square(10)
print(first_square.calculate_perimeter())
first_square.change_size(-2)
print(first_square.calculate_perimeter())
first_rectangle.what_am_i()
first_square.what_am_i()

# 4
class Horse():
    def __init__(self, breed, color, rider):
        self.breed = breed
        self.color = color
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

charlie = Rider("Charles M.")
polly = Horse("Clydesdale", "Pink", charlie)
print(polly.rider.name)

