# Write a function that orders a list least to greatest by comparing the current index value to the next 
# index value. If the next index is lower than the current index, swap the values. continue this until 
# you reach the end of the list

import timeit
start = timeit.default_timer()

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

# Dre's Solution

# def bubbleSortDre(nums: list) -> list:
#     for i in range(len(nums)):  # Iterating from front to back of the list
#         # Since the last indexs traversed in the pervious iteration will always
#         # be the largest vbalue, decrease the number of indices traversed by 1
#         # With a list length 5, in the 1st iteration we traverse 5 indices, then 
#         # in the 2nd iter, 4 indices, 3rd iter we will traverse 3 indices, etc.
#         for currentIndex in range(0, len(nums) - i - 1):  # for each index
#             # Checking if the next index is greater than the current index
#             if nums[currentIndex] > nums[currentIndex + 1]:
#                 # Swap the values if true
#                 nums[currentIndex], nums[currentIndex + 1] = nums[currentIndex+1], nums[currentIndex]
#     return nums

# numList = [12, 34, 56, 78, 90, 89, 67, 45, 23]
# bubbleSortDre(numList)
# print(numList)

stop = timeit.default_timer()
print('Time: ', stop - start)  