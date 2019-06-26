class Rectangle():
    # Class variable recs
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width,self.len))

    def print_size(self):
        print("""{} by {}""".format(self.width, self.len))

r1 = Rectangle(10,24)
r2 = Rectangle(20,40)
r3 = Rectangle(100,200)

print(Rectangle.recs)

# magic methods
class Lion:
    def __init__(self, name):
        self.name = name

    # __repr__ is what the print statement returns
    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)

# __add__ method is used when '+' is used in an expression
class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)

# 'is' returns true if two objects point to same object

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
#true
print(bob is same_bob)

another_bob = Person()
#false
print(bob is another_bob)

# can use 'is' to check if a variable is 'None'

x = 10
if x is None:
    print("X is None :( ")
else:
    print("X is not None")

x = None
if x is None:
    print("x is None")
else:
    print("x is None :(")


# Challenges

class Square:
    square_list = []

    def __init__(self,length):
        self.length = length

        self.square_list.append(["{} squared".format(self.length)])

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.length,self.length,self.length,self.length)
sq1 = Square(10)
sq2 = Square(20)
sq3 = Square(30)

print(Square.square_list)
print(sq1)
print(sq2)
print(sq3)

# 3
def the_same(first, second):
    if first is second:
        return True
    else:
        return False

print(the_same(sq1, sq2))
print(the_same(sq3, sq3))




