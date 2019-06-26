import random
def hangman(word):
    wrong = 0
    stages = ["",
              "_______   ",
              "|          ",
              "|      |   ",
              "|      0   ",
              "|     /|\  ",
              "|     / \  ",
              "|          "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:\
                 wrong]))
        print("You lose! It was {}.".format(word))




random_words = ["doggy", "kitty", "abercrombie"]

random_number = random.randint(0, len(random_words)-1)

hangman(random_words[random_number])

