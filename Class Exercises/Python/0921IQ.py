# Write a function that takes in a string of numbers and return the text message. Write 3 units test validating your function
# Given a string consisting of 0-9,
#     find the string that is created using
#     a standard phone keypad
#     | 1        | 2 (abc) | 3 (def)  |
#     | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
#     | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
#     |     *    | 0 ( )   |     #    |
#     You can ignore 1, and 0 corresponds to space
#     >>> keypad_string("12345")
#     'adgj'
#     >>> keypad_string("4433555555666")
#     'hello'
#     >>> keypad_string("2022")
#     'a b'
#     >>> keypad_string("")
#     ''
#     >>> keypad_string("111")
#     ''
#     '''

# If 1  is in the first index, return invalid
# loop
# If 2 is in the point index, add A
# If 2 is in the 2nd point index, remove A, add B
# If 2 is in the 3rd point index, remove B, add C

# dictionary = {
#     2: 'A', 22: 'B', 222: 'C',
#     3: 'D', 33: 'E', 333: 'F',
#     4: 'G', 44: 'H', 444: 'I',
#     5: 'J', 55: 'K', 555: 'L',
#     6: 'M', 66: 'N', 666: 'O',
#     7: 'P', 77: 'Q', 777: 'R', 7777: 'S',
#     8: 'T', 88: 'U', 888: 'V',
#     9: 'W', 99: 'X', 999: 'Y', 9999: 'Z',
# }

convertedString = []
appendNumString = []

def t9keypad(keypad_string):
    if ("111" in keypad_string):
        print("C") 
        convertedString
    elif ("11" in keypad_string):
        print("B")
    elif ("1" in keypad_string):
        print("A")

    # for i in keypad_string:
    #     appendNumString.append(i)
    #     if appendNumString[0] == "1":
    #         print("Invalid entry.")


t9keypad("111")
# t9keypad("4433555555666")
