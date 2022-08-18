# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:

# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".

# Need input list, number of output, and number of different transformation (unique output)

morseCodeDict = {
    'a': ".-",    'b': "-...",    'c': "-.-.",
    'd': "-..",    'e': ".",    'f': "..-.",
    'g': "--.",    'h': "....",    'i': "..",
    'j': ".---",    'k': "-.-",    'l': ".-..",
    'm': "--",    'n': "-.",    'o': "---",
    'p': ".--.",    'q': "--.-",    'r': ".-.",
    's': "...",    't': "-",    'u': "..-",
    'v': "...-",    'w': ".--",    'x': "-..-",
    'y': "-.--",    'z': "--.."
}

def convertToMorseCode(sentence):
    sentence = sentence.lower()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += morseCodeDict[character] + " " 
    return encodedSentence

wordList = ["gin","zen","gig","msg"]
result = convertToMorseCode(wordList)
print(result)


