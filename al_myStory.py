#Anna Lieb
#5/17/18
#CSP 2018
#al_myStory.py

import random
import time

def checkInput(choice):
    while choice != 1 and choice != 2:
        print("You have entered an invalid choice. ")
        choice = int(input("Enter choice 1 or 2: "))

def intro():
    print('''It's a beautiful day in Princeton, and you decide to take a nap in
the campus gardens. But when you wake up, everything is different! All of the
oak trees are gone, replaced with luscious ferns. Suddenly, a man appears out
of the jungle. That's when you notice a small path, leading into the dense
leaves. Do you 1) Approach the man or 2) Follow the path?''')
    choice1 = int(input("Enter choice 1 or 2: "))
    checkInput(choice1)
    return choice1

def approachMan():
    print('''You greet the man and he leads you to a freshwater lake. He has a
filter that makes the water drinkable. You're not sure if you trust him, but
you're so thirsty that you drink the water anyways. You feel refreshed, and
decide to go to explore the forest with the man...''')
    time.sleep(10)

def dinoAttack():
    time.sleep(3)
    numDinos = random.randint(2,6)
    print('''Oh no! A pack of''', numDinos, '''dinosaurs are running up the
path! Do you want to 1) Run away or 2) Fight? ''')
    choice2 = int(input("Enter choice 1 or 2: "))
    checkInput(choice2)
    if numDinos > 3 and choice2 == 2:
        print('''Unfortunately, the pack was too large and you and the
explorer were not able to fend off the dinosaurs! You did not survive.''')
    else:
        print('''Luckily, you and the explorer were able to survive the
dinosaurs. Congratulations!''')

def followPath():
    print('''You follow the path through the beautiful jungle, although you
can't help but feel uneasy. Soon, you come across a freshwater lake. You're
thirsty, but you hesitate before drinking. Who knows what could be in that
water? Do you 1) Drink the water or 2) Keep walking?''')
    choice3 = int(input("Enter choice 1 or 2: "))
    checkInput(choice3)
    return choice3

def drinkWater():
    print('''Oh no! It turns out the lake water was more toxic than it looked.
You did not survive.''')

def endStory():
    repeat = input("Would you like to start the story over? y/n ")
    if repeat ==  "y":
        main()
    else:
        print("Goodbye. ")

def main ():
    choice1 = intro()
    if choice1 == 1:
        approachMan()
        dinoAttack()
        choice3 = None
    else:
        choice3 = followPath()
    if choice3 == 1:
        drinkWater()
    elif choice3 == 2 and choice1 != 1:
        dinoAttack()
    endStory()
        
main()
