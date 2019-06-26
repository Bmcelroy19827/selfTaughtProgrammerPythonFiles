tv = ["GOT",
      "Narcos",
      "Vice"]

#i= 0
#for show in tv:
#    new = tv[i]
#    new = new.upper()
#    tv[i] = new
#    i += 1

# other(better) way
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

# range function takes two parameters, where sequence starts and stops. includes first number but not end
for i in range(1,11):
    print(i)

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")

# 'break' statement stops a loop

qs = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?"]
#n = 0
#while True:
#    print("Type q to quit")
#    a = input(qs[n])
#    if a == "q":
#        break
#    n = (n + 1) % 3

# 'Continue' statement stops the current iteration and moves to the next
for i in range (1,6):
    if i == 3:
        continue
    print(i)

# Challenges

#1
shows = ["The Walking Dead", "Entourage", "The Sapranos", "The Vampire Diaries"]
for show in shows:
    print(show)

#2
for i in range(25,51):
    print(i)

#3
for i, show in enumerate(shows):
    print("The show is {} and the index in list is {}".format(show, i))

#4
listedNumbers = [1,2,3,4,5]
while True:
    guess = input("Guess a number (q to quit): ")
    
    if guess == "q":
        break
    else:
        try:
           guess = int(guess)
        except:
            print("That's not a number")
            continue
        
    
    try:
        found = listedNumbers.index(guess)
        print("Number is in list")
    except:
        print("Number not in list")

#5
first_list = [8, 19, 148, 4]
second_list = [9, 1, 33, 83]
finished_list = []
for i in first_list:
    for j in second_list:
        product = i * j
        finished_list.append(product)
print(finished_list)

