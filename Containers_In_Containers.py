# lists in a list
lists = []
rap = ["Kanye West",
       "Jay Z",
       "Eminem",
       "Nas"]

rock = ["Bob Dylan",
        "The Beatles",
        "Led Zeppelin"]

djs = ["Zeds Dead",
       "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)
print(lists[0][1])
print("---------------------------------------------")

# append to rap lists updates in lists as well
rap.append("Kendrick Lamar")
print(rap)
print(lists)
print("---------------------------------------------")
# tuple inside a list
locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)
print("---------------------------------------------")
# lists inside a tuple

eights = ["Edgar Allan Poe", "Charles Dickens"]

nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)
print(authors)
print("---------------------------------------------")
# Dictionary inside a list and a tuple

bday = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"}

my_list = [bday]
my_tuple = (bday)
print(my_list)
print(my_tuple)
print("---------------------------------------------")

# list, tuple, or dictionary as value in a dictionary

ny = {"location":
      (40.7128, 74.0059),

      # list as value
      "celebs":
      ["W. Allen",
       "Jay Z",
       "K. Bacon"],

      # dictionary as value
      "facts":
      {"state": "NY",
       "country": "America"}

      }

print(ny)

#Challenges
# 1
favorite_musicians = ["Metallica", "Megadeth", "The Dead South", "Avenged Sevenfold"]
# 2
where_i_lived = [(40.0191, -81.5814),(39.9257, -81.5840)]
# 3
facts_about_me = {"height": "5'8\"",
                  "favorite color": "Blue",
                  "favorite author": "Orwell"}
#4
user_choice = input("Ask for my 'height', 'favorite color', or 'favorite author': ")
if user_choice in facts_about_me:
    print(facts_about_me[user_choice])
else:
    print("Sorry, that choice is not valid")

#5
metallica_songs = ["The Four Horsmen", "Call of Ctulu", "Battery", "Shortest Straw", "Through the never"]
megadeth_songs = ["Hook in mouth", "Hanger 18", "Disconnect"]
dead_south_songs = ["In Hell I'll be in good company",]
avenged_sevenfold_songs = ["Critical Acclaim", "Little Piece of heaven", "Nightmare"]
favorite_songs = { favorite_musicians[0]: metallica_songs,
                   favorite_musicians[1]: megadeth_songs,
                   favorite_musicians[2]: dead_south_songs,
                   favorite_musicians[3]: avenged_sevenfold_songs}

band = input("Enter 'Metallica', 'Megadeth', 'The Dead South', or 'Avenged Sevenfold' to see a list of songs: ")
if band in favorite_songs:
    print(favorite_songs[band])
else:
    print("Band not found")


                    

