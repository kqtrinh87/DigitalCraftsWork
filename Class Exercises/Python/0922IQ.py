# Mastermind
# A low-level implementation of the classic game “Mastermind”. We need to write a program that generates a four-digit random code and the user needs to guess the code in 10 tries or less. If any digit out of the guessed four-digit code is wrong, the computer should print out “B”. If the digit is correct but at the wrong place, the computer should print “Y”. If both the digit and position is correct, the computer should print “R”.

# # Generate a random 4 digit number
# from random import randint

# random4Digits = randint(1000,9999)
# arrayRandom4Digits = list(str(random4Digits))
# print(arrayRandom4Digits)
# # Take user input of of 4 digit
# user4digits = input("Type in your guess of the 4 digits number: ")

# # If not in correct format, print out invalid and retry
# def checkInputValidity(user4digits):
#     if len(user4digits) != 4 or user4digits.isdigit() == False:
#         # Make sure user input is exactly 4 and is digits only
#         print("Invalid entry. Make sure to have exact 4 digits.")

# arrayUser4Digits = list(str(user4digits))

# print(arrayUser4Digits)
# def checkingNumbers():
#     for num in arrayUser4Digits:
#         if num == arrayRandom4Digits:
#             print("B")
#         # if b in arrayRandom4Digits:
        

# # if the digit is not in the input, print out a B in place of that digit

# # if the digit is in the input but not in the correct position, print out a Y in place of that digit

# # if the digit is in the input and in the correct position, print out a R in place of that digit

# checkInputValidity(user4digits)
# checkingNumbers()


# # after 10 tries, game over
# # if guess correctly, print winner

import random

# Step 1: Creat a function that generate a random 4 digits number
def mastermind():
    answer = generateNumber()
    turns = 0
    win = False
    print('Welcome to MasterMind!')
    while turns <= 10 and win == False:
        guess = input('Enter a number: ')
        if checkGuess(guess, answer) == True:
            win = True
            print("You're Won! The answer is ", answer)
        turns += 1
        print("Turn: ", turns)
    if turns >= 10:
        print("You've lost! The correct answer is", answer)

def generateNumber() -> str:
    number = ''
    for num in range(0,4):
        number += str(random.randint(0,9))
    return number

# Check if the guess is equal to the answer
def checkGuess(guess: str, answer: str) -> bool:
    hint = ''
    for i in range(0,4):
        # If the guess at this index is the same as the answer, add a R
        if guess[i] == answer[i]:
            hint += 'R'
        # Check if answer contains the guessed number, add a Y
        elif guess[i] in answer:
            hint += 'Y'
        # If the number is not in the answer at all, add a B
        else:
            hint += 'B'
    print(hint)
    return hint == 'RRRR'

mastermind()
