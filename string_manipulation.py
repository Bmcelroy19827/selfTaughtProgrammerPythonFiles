# triple Strings - use triple quotes if a string spans more than one line

""" Line one
    Line two
    Line three
"""

# strings are iterable and have an index starting at zero

author = "Kafka"

for i in range (0,len(author)):
    print(author[i])
print("-------------------------------")
for i in author:
    print(i)

# Negative indexes
print("------------------------------")
print(author[-1])

# Strings are immutable
# concatenation
dr_seus = "Cat " + "in " + "the " + "hat. "
print(dr_seus)

# string multiplication
print((dr_seus * 3))

# Change Case
print(dr_seus.upper())
print(dr_seus.lower())

lower_case_first = "this sentence started with lower case 't'"
print(lower_case_first.capitalize())

# formatting a string
formatted_cat = "The {}".format(dr_seus.lower())
print(formatted_cat)
# more than one set of brackets
author = "William Faulkner"
year_born = "1897"
formatted_faulkner = "{} was born in {}.".format(author, year_born)
print(formatted_faulkner)

'''

n1 = input("Enter a noun: ")
v = input("Enter a verb: ")
adj = input("Enter an adjective: ")
n2 = input("Enter another noun:")

madlib = """The {} {} the {} {}
         """.format(n1, v, adj, n2)
print(madlib)

'''

# split
split_up = "Let's split this at the period. Here's the second part.".split(".")
print(split_up)

# Join
put_back_together = ".".join(split_up)
print(put_back_together)

# Strip Space
spaces = "      The        "
stripped = spaces.strip()
print(stripped)

# Replace
equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)

# find first index of an occurence
# exception raised if no match found
print("animals".index("m"))
try:
    print("animals".index("z"))
except:
    print("Not found.")
# 'in' and 'not in'

# escape a character with '\', '\n' for newline

# slicing

fict = ["Tolstoy",
        "Camus",
        "Orwell",
        "Huxley",
        "Austin"]
print(fict[0:3])

ivan = """In a place of death there was light."""
print(ivan[:19])
print(ivan[19:])

# Challenges

# 1
for i in "Camus":
    print(i)

# 2

userLiterature = input("Enter a type of literature(letter, poem, book, etc): ")
userName = input("Enter a place or name: ")
print("Yesterday I wrote a {}. I sent it to {}!".format(userLiterature, userName))

#3

print("aldous Huxley was born in 1894".capitalize())


#4
expression = "Where now? Who now? When now?"
print(expression.split("?"))

#5
listed_sentence = ["The", "fox", "jumped", "over", "the", "fence", "."]
print(" ".join(listed_sentence[:6]) + ".")

#6
print("A screaming comes across the sky.".replace("s", "$"))

#7
print("Hemingway".index("m"))

#8
print("\"Quotes are here\"")

#9
print("three " + "three " + "three")
print("three " * 3)

#10

sample_sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
print(sample_sentence[:sample_sentence.index(",")])



