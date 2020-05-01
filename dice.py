import random
import sys
import time


def diceRoll():
    for i in range(1):
        num = (random.randint(1, 6))
        print("Rolling....")
        time.sleep(1)
        print("you rolled a " + str(num))
        time.sleep(1)
        while True:
            print("Want to roll again?\ny or n?")
            again = input()
            if again == 'n':
                print('Ok,')
                time.sleep(0.5)
                print('Bye')
                sys.exit()
            elif again == 'y':
                diceRoll()
            else:
                print("Please press 'y' for Yes or 'n' for No.")
                break


while True:
    print("Press 'r' to roll dice:")
    r = input()
    if r != 'r':
        print("Worng Key!")

    else:
        diceRoll()
        break
