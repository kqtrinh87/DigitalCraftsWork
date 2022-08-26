# Write a function that orders a list least to greatest by comparing the current index value to the next 
# index value. If the next index is lower than the current index, swap the values. continue this until 
# you reach the end of the list

import timeit
start = timeit.default_timer()

def bubbleSort(numList):
    # We want to stop passing through the list as soon as we pass through without swapping any elements
    hasSwapped = True 
    while(hasSwapped): # While hasSwapped is True
        hasSwapped = False # Declare this hasn't swapped
        for i in range(len(numList) - 1): # For each index in the range through the size of number list 
            if numList[i] > numList[i+1]: # If the selected index is greater than the next index
                numList[i], numList[i+1] = numList[i+1], numList[i] # Swap the numbers
                hasSwapped = True # Declare this has swapped 

numList = [12,34,56,78,90,89,67,45,23]
bubbleSort(numList)
print(numList)

stop = timeit.default_timer()
print('Time: ', stop - start)