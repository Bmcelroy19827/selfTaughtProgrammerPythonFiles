#Import OS to help make paths that don't conflict across operating systems
import os

print(os.path.join("Users","bob","st.txt"))

# open function has several modes that are passed some include:
# "r" opens for read only, "w" opens for writing only, "w+" opens for reading and writing

# open file, write to it, and close it

st = open("st.txt", "w")
st.write("Hi Python!")
st.close()

# same as above but auto closes

with open("st.txt", "w") as f:
    f.write("This closes automatically")

# reading from a file
with open("st.txt", "r") as f:
    print(f.read())

# save contents of a file into a list to use later

my_list = list()

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)

# CSV files (comma separated values) natively supported by python.

import csv

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")

    w.writerow(["one","two","three"])

    w.writerow(["four", "five", "six"])

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

# Challenges

# 1

#with open("D:\Programming\StackerControl.txt","r") as f:
#    print(f.read())

# 2

user_answer = input("What is your favorite color? " )
with open("userAnswer.txt", "w") as f:
    f.write(user_answer)
with open("userAnswer.txt", "r") as f:
    print(f.read())

# 3

movies_lists = [["Top Gun", "Risky Business", "Minority Report"],
                ["Titanic", "The Revenant", "Inception"],
                ["Training Day", "Man on fire", "Flight"]]

string_for_csv = ""
for row in movies_lists:
    string_for_csv += ",".join(row)
    string_for_csv += "\n"
        

with open("movies.csv", "w") as f:
    f.write(string_for_csv)
with open("movies.csv", "r") as f:
    print(f.read())

    

