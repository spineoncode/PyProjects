import random

userInput = input("Enter a range of no.\n>>> ").split("to")
userInput[0] = int(userInput[0])
userInput[1] = int(userInput[1])

guess = random.randint(userInput[0], userInput[1])

guessNo = 0

while True:
    userGuess = int(input("Guess The Number?\n>>> "))
    if (userGuess == guess):
        print("Hooray! You Guessed It Right!")
        if guessNo < 5:
            print(f"And that too only in {guessNo}")
        elif guessNo < 10:
            print(f"And the no of tries you took is {guessNo}.")
        else:
            print("But You Took Too Many Tries")
        break
    elif userGuess > guess:
        print("Your guess is higher! a little or more you take care...")
        guessNo += 1
    elif userGuess < guess:
        print("Your guess is lower! a little or more you take care...")
        guessNo += 1
    else:
        guessNo += 1
