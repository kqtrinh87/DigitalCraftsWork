from re import I


name = 'Khanh Trinh '

# In order to retrieve the length of a string or list
# use len() function

# print(len(name))

# This apparently print out the first letter of name (Not a list)
# print(name[0])

# drinks = ['Sprite', 'Dr.Pepper', 'Coke', 'Pepsi']

# This print out the class of the number of the items inside the array
# print(type(len(drinks)))

# This print out the number (int) of the number of items inside the array
# print(len(drinks))

# length_of_drinks = len(drinks)
# print(length_of_drinks)

# This is a (For) loop that print out the index in order of the array in each line.
# "For [each] item in [list] list, print [each] item until nothing remains"
# for item in drinks:
#     print(item)

# (Same Results from Above) While loop doing the same
# loop = 0
# while loop < len(drinks):
#     print(drinks[loop])
#     loop = loop + 1

# Iterate through a string using a for loop
# Name is the string using a for loop
# letter is a variable being created and the loop is automatically placing
# the value at each index in the letter variable

# Each letter in a string is its own index. K -> 0, H -> 2, etc
# for letter in name:
#     print(letter)
    
# Iterate through my name using a while loop
# num = 0
# while num < len(name):
#     print(name[num])
#     num = num + 1

# Which of these numbers is divided 4 evenly? If yes, print.
# numbers = [423, 6234, 5662, 1234, 8905, 784]
# for dividedby4evenly in numbers:
#     # %  is a remainder after dividing.
#     if dividedby4evenly % 4 == 0:
#         print(dividedby4evenly)

# Which of these numbers is an odd number? If yes, print.
# numbers2 = [5, 8, 10, 14, 20, 53, 91]
# for oddnums in numbers2:
#     # %  is a remainder after dividing.
#     if oddnums % 2 == 1:
#         print(oddnums)

# Using the list of numbers provided above, allow a user to pick
# a number to divide each number in the list by and only print
# numbers that are divisible by the number the user inputs.

# numbers3 = [5, 8, 10, 14, 20, 53, 91]
# try:
#     userpicksnumbers = int(input('Enter a number to divide by: '))
#     for userinput in numbers3:
#         if userinput % userpicksnumbers == 0:
#             print(userinput)

# except:
#     print('This program can only take numbers')

# Way to print out memory value or location
# print('Memory Address of Name list of 1st letter: ', hex(id(name)))
# print('Memory Address of Name list of 2nd letter: ', hex(id(name[1])))

# Lexicon comparsion
# mysteryLetter = 'b'
# firstNameLetter = 'd'
# if firstNameLetter < mysteryLetter:
#     print('firstname comes before mysteryLetter')
# else: 
#     print('mysteryLetter comes before the firstname')

# Place students inside of a breakout room depending on their firstname. If
# the name comes before letter "i", then place in breakoutroom1, else in
# breakroom2

# students = input('Type in a list of students: ')
# students = ['Matt', 'Carlos', 'An', 'Jordan B.']
# breakoutroom1 = []
# breakoutroom2 = []
# cutoffLetter = 'i'

# for element in students:
#     if element[0].lower() <= cutoffLetter:
#         breakoutroom1.append(element)
#     elif element[0].lower() > cutoffLetter:
#         breakoutroom2.append(element)

# print(breakoutroom1)
# print(breakoutroom2)

#----------------------------------------------------------------------------------
# Python has a list of reserved words that cannot be used as variables
# or function names

# String Concatenation

diceroll = 9
firstName = 'Khanh'
lastName = 'Trinh'
fullName = firstName + ' ' + lastName + ' ' + str(diceroll)
print(fullName)

# Practice to allow user input to create firstName, lastName, and favorite number.
