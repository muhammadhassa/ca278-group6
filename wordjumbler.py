import random

class Jumbler():
    def __init__(self, user_choice):
        self.choice = user_choice

    def start(self):

        if (self.choice == "4"):
            exit("You have left the game!")
        else:
            self.loadr()

    def loadr(self):
        if (self.choice == "1"):
            fileopen = open("animals.txt", "r")
        elif (self.choice  == "2"):
            fileopen = open("countries.txt", "r")
        elif (self.choice == "3"):
            fileopen = open("sports.txt", "r")
        for i in fileopen:
            self.data(i)

    def data(self, b):
        l = list(b.rstrip().upper())
        random.shuffle(l)
        result = "".join(l)
        userData = self.terminal(result)
        if (b.rstrip().upper() == userData.rstrip().upper()):
            print("\n correct answer")

        else:
            exit("Wrong answer, Game Over!")

    def terminal(self, data):
        print("************")
        print("" + data + "")
        print("************")
        answer = input("Enter word correctly:")
        return answer


def main():
    user_choice = input(""" Choose your word jumbler category?\n
    1. Animals
    2. Countries
    3. Sports
    4. Exit game
    """)
    game = Jumbler(user_choice)
    game.start()



if __name__ == '__main__':
    main()