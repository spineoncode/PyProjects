import random

compChose = random.randint(1000, 9999)
userGuess = ["-", "-", "-", "-"]
noOfGuess = 0

print("You Have to guess the no I chose!")
while True:
    guess = int(input("Your number: "))
    if guess == compChose:
        if noOfGuess <= 1:
            print("Bruh! You Took Me Down In One Guess! For Sure a Mastermind!")
        elif noOfGuess <= 3:
            print(f"You Are On The Way To A Mastermind! You Did It in Just {noOfGuess} Guesses.")
        else:
            print(f"You Got It Correct In {noOfGuess} Guesses!")
        exit(0)
    elif guess != compChose:
        gotCorrect = 0
        guess_1 = str(guess)
        for index, item in enumerate(str(compChose)):
            if item == guess_1[index]:
                userGuess[index] = guess_1[index]
                gotCorrect += 1
        userGuess_made = " ".join(userGuess)
        print(f"You Got {gotCorrect} Digit(s) Correct\n{userGuess_made}")
        if guess > compChose:
            print("The Number You Chose Is Greater Than I did!")
        elif guess < compChose:
            print("The Number You Chose Is Less Than I did!")
        noOfGuess += 1
