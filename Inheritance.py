
class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def print_size(self):
        print("""{} by {}""".format(self.width, self.len))

class Square(Shape):
    
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("""I am {} by {}""".format(self.width, self.len))

a_square = Square(20,20)
print(a_square.area())
a_square.print_size()

# Composition
class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)


