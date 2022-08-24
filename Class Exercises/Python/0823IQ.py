# Write a function that orders a list least to greatest by comparing the current index value to the next 
# index value. If the next index is lower than the current index, swap the values. continue this until 
# you reach the end of the list

def bubbleSort(numList):
    for num in range(len(numList)-1,0,-1): # For Loop: for each number in the range through the size of number list, from last index to first index.
        for x in range(num): # For Loop: for selected number in the range of selected number
            if numList[x]>numList[x+1]: # If the 1st selected num is greater than the number to its right
                temp = numList[x] # Save it temporarily (larger num)
                numList[x] = numList[x+1] # Replace the number with the 1st selected num with the number to its right
                numList[x+1] = temp # Replace the next index with temporarily number (larger num)

numList = [12,34,56,78,90,89,67,45,23]
bubbleSort(numList)
print(numList)