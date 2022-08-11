
# firstWord = input("Type in your first word you wish to compare to if it's an anagram: ")
# secondWord = input("Type in your second word you wish to compare with your first word: ")
# firstWord = firstWord.lower()
# secondWord = secondWord.lower()

# def quicksort(lst):
#     if not lst:
#         return []
#     return (quicksort([x for x in lst[1:] if x <  lst[0]])
#             + [lst[0]] +
#             quicksort([x for x in lst[1:] if x >= lst[0]]))

# firstWord = quicksort(firstWord)
# secondWord = quicksort(secondWord)

# if firstWord == secondWord:
#     print('Your two words are an anagram! :)')
# else: 
#     print('Your two words are NOT an anagram!. :(')

word1 = input('Type in a word: ')
word2 = input('Type in a word: ')

dict1 = {}
dict2 = {}

def anagram(word1, word2):
    dict1 = createDictFromWord(word1)
    dict2 = createDictFromWord(word2)
print(dict1 == dict2)

def createDictFromWord(word: str) -> dict:
    strDict = {}
    for letter in word1:
        if letter in strDict.keys():
            strDict[letter] = strDict.get(letter) + 1
        else:
            strDict[letter] = 1

        return strDict
