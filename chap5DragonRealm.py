#!/usr/bin/python3

import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.'''+"\n")


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will go to into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave ...'+"\n")
    time.sleep(2)
    print('It is dark and spooky ...'+"\n")
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and ...'+'\n')
    time.sleep(2)

    friendlyCave = random.randint(1,2)
    if chosenCave == str(friendlyCave):
        print('Give you his treasure!'+'\n')
    else:
        print('Gobbles you down in one bite!'+'\n')


#playAgain = 'yes'


def wantToPlay():
    print('Please let us know if you want to play the dragon game (yes or no)')
    choice = input()
    count = 1
    while choice != 'yes' and choice != 'no' and count<3:   #validate the user choice, and quit if choose wrong answer 3 times.
        count += 1
        print('Please choose again (yes or no)')
        choice = input()
#        print(choice, count)
    return choice

userChoice = wantToPlay()

while userChoice == 'yes' or userChoice == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('GAME OVER'+'\n')
    userChoice = wantToPlay()
    count=0


