# Without using the built-in python library, sort an array 
# of integers from least to greatest

numList = [423, 53123, 5, 892, 94, 23453, 75, 2725, 64, 904]

#Bubble Sorting Method
for x in range(len(numList)): 
    for y in range(x + 1, len(numList)): 
 
        if numList[x] > numList[y]: 
           numList[x], numList[y] = numList[y], numList[x]

print(numList)
# print (numList[::-1])

## Selection Sorting Method
# for x in range(0,len(numList)-1,1): # Logic of Selection Sort
#     min = x
#     for y in range(x+1, len(numList),1):
#         if (numList[y]<numList[min]):
#             min = y
#     numList[x], numList[min] = numList[min], numList[x]

# print(numList)

## Quick Sorting Method
# def quicksort(lst):
#     if not lst:
#         return []
#     return (quicksort([x for x in lst[1:] if x <  lst[0]])
#             + [lst[0]] +
#             quicksort([x for x in lst[1:] if x >= lst[0]]))

# print(quicksort(numList))