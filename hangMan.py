#!/usr/bin/python3

import random
import os

def checkRepeat(char, full):
    foundUsed = False

    for i in full:
#        print('checking: ', i, 'against', char)
        if char == (i or ' '):
            print('you cannot enter an empty space or already tried character')
            foundUsed = True
            return char, full, foundUsed

    if foundUsed == False:
        full.append(char)

#    print('updated list: ', full)
    return char, full, foundUsed


def checkHit(guess, secretChars):
    guessid=[]
    for i in range(len(secretChars)):
        if guess == secretChars[i]:
#            print('Bingo')
            guessid.append(i)
    return guessid

def printMask(mask):
    for i in mask:
        print(i, end=' ')
    return

def printHangman(missedGuess):
    if missedGuess == 0:
        print(' +---+')
        print('     |')
        print('     |')
        print('     |')
        print('   =====')
    elif missedGuess == 1:
        print(' +---+')
        print(' O   |')
        print('     |')
        print('     |')
        print('   =====')
    elif missedGuess == 2:
        print(' +---+')
        print(' O   |')
        print(' |   |')
        print('     |')
        print('   =====')
    elif missedGuess == 3:
        print(' +---+')
        print(' O   |')
        print('/|   |')
        print('     |')
        print('   =====')
    elif missedGuess == 4:
        print(' +---+')
        print(' O   |')
        print('/|\  |')
        print('     |')
        print('   =====')
    elif missedGuess == 5:
        print(' +---+')
        print(' O   |')
        print('/|\  |')
        print('/    |')
        print('   =====')
    elif missedGuess == 6:
        print(' +---+')
        print(' O   |')
        print('/|\  |')
        print('/ \  |')
        print('   =====')

def checkComplete(mask):
    for i in mask:
        if i == '-':
            return False
    return True



#print('please enter a secret word.\n')
#secret = input()

print('Randomly picking a word from Shakespeare, And you have SEVEN chance to guess the letters in the word')
quote = 'full fathom five thy father lies of his bones are coral made those are pearls that were his eyes nothing of him that doth fade but doth suffer a sea-change into something rich and strange'
sequence = quote.lower().split()
secret = random.choice(sequence)

#secret = 'here'
secretChars = list(secret)
secretLen = len(secret)

mask = [u'-'] * secretLen
printMask(mask)
print()

#print(secretLetters)

print('please guess a letter')
userGuess = input()

missedGuess=0
alreadyGuessed = []
isRepeat = False

#guess, alreadyGuessed, isRepeat = checkRepeat(userGuess, alreadyGuessed)

#tries = 0
while missedGuess < 6:
    guess, alreadyGuessed, isRepeat = checkRepeat(userGuess, alreadyGuessed)
    while isRepeat is True:
#        os.system('clear')
        print('please guess a new letter')
        userGuess = input()
        guess, alreadyGuessed, isRepeat = checkRepeat(userGuess, alreadyGuessed)

    hitResult = checkHit(guess, secretChars)
#    print(hitResult)

    if hitResult:
        print('Bingo, the letter', guess,'is in position', end=' ')
        for i in hitResult:
            print(i+1, end=' ')
            mask[i] = secretChars[i]
        print()
        printHangman(missedGuess)
        printMask(mask)
        print()
    else:
        missedGuess += 1
        print('Sorry, you still have', 7-missedGuess,'chance(s).')
        printHangman(missedGuess)
        printMask(mask)
        print()

    if checkComplete(mask) == True:
        print('Congratulations, you won! The secret is: ', secret)
        break

    print('please enter next guess')
    userGuess = input()
#    tries += 1

#print('you guessed', alreadyGuessed, 'and the secret is', secret,'adding a test line for github')
if checkComplete(mask) == False:
    print('Sorry you lose! your final result is ', end=' ')
    printMask(mask)
    print()
    print('The secret word is :',secret)