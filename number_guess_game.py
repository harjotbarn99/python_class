import random

number = random.randint(1,100)

correct = False

tries = 0
choice = None

while not correct:
    tries += 1
    try:
        choice = input("type a number : ")
        if choice == "end":
            break
        choice = int(choice)
    except:
        print("'",choice,"' is not a number")
        continue
    if number == choice:
        correct = True
    else:
        print("wrong choice")
        if choice > number:
            print("The number is less than your ",choice)
        else:
            print("The number is greater than your ",choice)
if choice == "end":
    print("game over")
    print("you were not able to guess the correct number which was ",number)
else:
    print("congratulations! you guessed it right.\nThe number was ",number)
    print("you took ",tries," tries")

