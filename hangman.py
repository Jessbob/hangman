import random


def hangman():
    word = random.choice(["lego", "minecraft", "fortnite", "roblox"])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessMade = ""

    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessMade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You Win!!!")
            break
        print("Guess the word: ", main)
        guess = input()

        if guess in validLetters:
            guessMade = guessMade + guess
        else:
            print("Enter a valid letter")
            guess = input()
        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print("9 turns left")
                print("|```````````|")
                print("|           |")
                print("|           |")
                print("|           |")
                print("|           |")
                print("|___________|")

            if turns == 8:
                print("8 turns left")
                print("|```````````|")
                print("|           |")
                print("|     0     |")
                print("|           |")
                print("|           |")
                print("|___________|")

            if turns == 7:
                print("7 turns left")
                print("|```````````|")
                print("|           |")
                print("|     0     |")
                print("|     |     |")
                print("|           |")
                print("|___________|")

            if turns == 6:
                print("6 turns left")
                print("|```````````|")
                print("|           |")
                print("|     0     |")
                print("|     |     |")
                print("|    /      |")
                print("|___________|")

            if turns == 5:
                print("5 turns left")
                print("|```````````|")
                print("|           |")
                print("|     0     |")
                print("|     |     |")
                print("|    / \    |")
                print("|___________|")

            if turns == 4:
                print("4 turns left")
                print("|```````````|")
                print("|           |")
                print("|   \ 0     |")
                print("|     |     |")
                print("|    / \    |")
                print("|___________|")

            if turns == 3:
                print("3 turns left")
                print("|```````````|")
                print("|           |")
                print("|   \ 0 /   |")
                print("|     |     |")
                print("|    / \    |")
                print("|___________|")

            if turns == 2:
                print("2 turns left")
                print("|`````|`````|")
                print("|           |")
                print("|   \ 0 /   |")
                print("|     |     |")
                print("|    / \    |")
                print("|___________|")

            if turns == 1:
                print("1 turns left")
                print("|`````|`````|")
                print("|     |     |")
                print("|   \ 0 /   |")
                print("|     |     |")
                print("|    / \    |")
                print("|___________|")

            if turns == 0:
                print("You Lose")
                print("|`````|`````|")
                print("|     |     |")
                print("|     0     |")
                print("|    /|\    |")
                print("|    | |    |")
                print("|___________|")


name = input("Enter your name ")
print("Welcome", name)
print("----------------------------------------------")
print("Try to guess the word in less than 10 attempts")
hangman()
print()
