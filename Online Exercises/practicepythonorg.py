# # Exercise 1
# name = input("What is your name: ")
# age = int(input("How old are you: "))
# year = 2022 - age + 100
# print(name + ", you will be 100 years old in the year " + str(year))

## pynative.com Exercise 1
# Given two integer numbers return their product only if the
# product is equal to or lower than 1000, else return their sum.

number1 = int(input('Enter 1st number: '))
number2 = int(input('Enter 2nd number: '))


def productOrSum(number1, number2):
    if number1 * number2 <= 1000: # Not working. Why is this wrong?
        print(number1 * number2)
    else:
        print(number1 + number2)

productOrSum(number1, number2)

# Solution #1
# def multiplication_or_sum(num1, num2):
#     # calculate product of two number
#     product = num1 * num2
#     # check if product is less then 1000
#     if product <= 1000:
#         return product
#     else:
#         # product is greater than 1000 calculate sum
#         return num1 + num2

# # first condition
# result = multiplication_or_sum(20, 30)
# print("The result is", result)

# # Second condition
# result = multiplication_or_sum(40, 30)
# print("The result is", result)