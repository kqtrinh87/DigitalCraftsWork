# Write a function that reads a file. Return and print the word in the file 
# appears the most
# Iterate through the file and return the words that appears the most. 
# i.e if the word 'the' appears 16 times, keep track of it are return it to 
# the function caller as well as print it to the screen

# file = open("C:/Users/kqtri/Documents/GitHub/web-ft-08-22/Code/python/week3/sample/theRoadNotTaken.txt","r")
file = open("C:/Users/kqtri/Documents/GitHub/web-ft-08-22/Code/python/week3/sample/theWasteLand.txt","r", encoding ="utf8")
# file = open("C:/Users/kqtri/Documents/GitHub/web-ft-08-22/Code/python/week3/sample/thisIsJustToSay.txt","r")
frequent_word = ""
frequency = 0 
words = []

# Traversing file line by line
for line in file:
    line_word = line.lower().replace(',','').replace('.','').replace('?','').replace('\n','').replace('(','').replace(')','').replace('—','').split(" ")
    # splits each line into words, removing spaces, punctuations from the input
    for w in line_word: 
        words.append(w); # Adding them to list words

for i in range(0, len(words)): # Finding the max occurred word
    count = 1; # Declaring count
    # print(words)
    words = list(filter(None, words)) # Remove all empty strings from list
    for j in range(i+1, len(words)): # Count each word in the file 
        if(words[i] == words[j]): 
            count = count + 1
             

    if(count > frequency): # If the count value is more than highest frequency then
        frequency = count; 
        frequent_word = words[i]; 

print("Most repeated word: " + frequent_word)
print("Frequency: " + str(frequency))
file.close()