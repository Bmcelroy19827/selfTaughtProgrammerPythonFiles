my_dict = {}
my_other_dict = dict()
print(my_dict)
print(my_other_dict)

facts = dict()
print("This is facts: " + str(facts))
# Add a value to facts
facts["code"] = "Pretty fun"
print(facts["code"])

# Dictionary key must be immutable, a list or dictionary cannot be a dictionary key

# use 'in' or 'not in' to check if a key is in a dictionary

bill = dict({"Bill Gates": "charitable"})
print(("Bill Gates" in bill))
print(("Bill Doors" not in bill))

# deleting a key-value pair from a dictionary
books = {"Dracula": "Stoker", "1984": "Orwell", "The Trial": "Kafka"}

print(books)

del books["The Trial"]
print(books)




