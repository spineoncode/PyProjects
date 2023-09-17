import random
if __name__ == "__main__":
    listOfWords = ["Namaste", "Hello", "Konnichiva"]

    compChose = listOfWords[random.randint(0, 2)].lower()
    # This can be shortened to 'compChose = random.choice(listOfWords).lower()'

    userGuess = ["-" for i in range(len(compChose))]
    try:
        for i in range(len(compChose) + 2):
            if "-" in userGuess:
                letter = input("Letter: ")
                if letter in userGuess:
                    print("You Have Already Guessed That Letter!")
                    continue
                else:
                    for index, item in enumerate(compChose):
                        if letter == item:
                            userGuess[index] = item
                [print(item) for item in userGuess]
            else:
                print("You Guessed it Right!")
                break
    except KeyboardInterrupt:
        print("Bye! See You Again")
        exit()
