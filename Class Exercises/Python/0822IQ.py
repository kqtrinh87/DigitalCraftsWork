# def isValid(test_str):
#     if len(test_str)%2 != 0: # len(test_str) is odd -> invalid!
#         return False 
#     charList = {'(':')','{':'}','[':']'} # initialize parentheses dict
#     stack = []

#     for char in test_str:
#         if char in charList.keys(): # push opening bracket to stack
#             stack.append(char)
#     else:
#         if stack == []: # closing bracket without matching opening bracket
#             return False
#         open_brac = stack.pop() # if closing bracket -> pop stack top

#     if char != charList[open_brac]: # not matching bracket -> invalid!
#         return False
#     return stack == []

# userInput = '[()]'
# print(isValid(userInput))

# ------------------------------------------------------------------
def isValid(s):
    pairs = {'(':')', '[':']', '{':'}'}
    length = len(s)
    openingBrackets = []    
     
    for i in range(length):
        if s[i] in pairs:
            openingBrackets.append(s[i])
        elif len(openingBrackets) == 0:
            return False
        elif pairs[openingBrackets.pop()] != s[i]:
            return False 
             
    if len(openingBrackets) > 0:
        return False
    else:
        return True

userInput = '[({)]'
print(isValid(userInput))