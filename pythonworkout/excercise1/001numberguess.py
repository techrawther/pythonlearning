

import random

def guessing_game():
    randomnumber = random.randint(1, 100)
    print(randomnumber)
    found = False
    while not found:
        x = int(input("Enter some number"))
        if(x > randomnumber):
            print("It is too high")
        elif(x < randomnumber):
            print("It is too low")
        elif(x == randomnumber):
            found = True
            print("You guessed right")
        else:
            print("Something is wrong")
            exit(1)

guessing_game()


