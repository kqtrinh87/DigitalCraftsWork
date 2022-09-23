# 6. In Python, given a string, if the string length is less than 3, repeat the letters that are present three times. If the string length is more than three, return a new string whith the first three letters repeated. See the example below. 

# # newStr3('Java') → 'JavJavJav'
# # newStr3('Chocolate') → 'ChoChoCho'
# # newStr3('ab') → 'ababab'

def newStr3(inputWord):
    if len(inputWord) >= 3:
        print(inputWord[0] + inputWord[1] + inputWord[2] + inputWord[0] + inputWord[1] + inputWord[2] +inputWord[0] + inputWord[1] + inputWord[2])
    if len(inputWord) < 3:
        print(inputWord[0] + inputWord[1] + inputWord[0] + inputWord[1] + inputWord[0] + inputWord[1])

newStr3('Java') #→ 'JavJavJav'
newStr3('Chocolate') #→ 'ChoChoCho'
newStr3('ab') #→ 'ababab'