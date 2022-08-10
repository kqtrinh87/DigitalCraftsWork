# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

# My Group
userNum = (input('Please type in a palindrome number: '))
reversedInput = (userNum[::-1])

# for x in userNum:
if userNum == reversedInput:
    print('%s is a palindrome' % userNum)
else:
    print('%s is not a palindrome' % userNum)

# Haven't complete for non-numbers input

# Haven't complete for non-numbers input

# Matt's Group
# numbers = (input('Please enter a number that has at least three characters: '))

# try:
#     checkInt = int(numbers)
#     if len(numbers) > 2:
#         palindrome = numbers[::-1]
#         if numbers == palindrome:
#             print('The number %s is a palindrome!' % numbers)
#         else:
#             print('The number %s is not a palindrome!' % numbers)
#     else:
#         print('Invalid entry.')
# except:
#     print('Invalid entry.')

# # Jonathan's Group
# word = input("Enter a word. ")
# half = len(word)/2
# half = int(half)
# print(word[0:half+1])
# print(word[len(word):half-1:-1])

# if word[0:half+1] == word[len(word):half-1:-1]:
#     print("It is a palindrome. ")
# else:
#     print("Not a palindrome. ")
