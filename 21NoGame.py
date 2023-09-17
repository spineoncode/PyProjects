import random


class NoGame:
    count = 0

    def __init__(self):
        whoFirst = input("Would You Like To Go First\n>>> ")
        if whoFirst == "yes":
            self.countUser()
        else:
            self.countUp()

    def checkFinal(self):
        if self.count >= 21:
            return True
        else:
            return False

    def countUp(self):
        print("\n" + "My Turn!")
        self.count += random.randint(1, 3)
        print([i for i in range(1, (self.count + 1))])
        if self.checkFinal():
            print("\nCongratulations! You Won!!!")
        else:
            self.countUser()

    def countUser(self, first=True):
        if first:
            print("\n" + "Your Turn!")
        a = int(input("How Many No Do You Wanna Enter: "))
        if a > 0:
            if a < 4:
                for i in range(a):
                    nxtNum = int(input("Enter The Number: "))
                    if (nxtNum > self.count):
                        if (nxtNum < (self.count + 2)):
                            self.count += 1
                            print([i for i in range(1, (self.count + 1))])
                    else:
                        print("You Lose! You Didn't entered a consecutive no..")
                        exit(0)
                if self.checkFinal():
                    print("\nYou Lose! Better Luck Next Time!")
                else:
                    self.countUp()
            else:
                print("You can't enter more than three numbers at once...")
                self.countUser(False)
        else:
            print("You can't enter more than three numbers at once...")
            self.countUser(False)


newGame = NoGame()
