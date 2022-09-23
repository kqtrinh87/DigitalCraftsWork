# Given an array containing None values fill in the None values with most recent value
# In python, write a function that takes in an array and returns the new array
numList = [1 ,2 , None, 4, 5, None, 7, 8, None , 10]

def fillInBlank(numList):
    for i in range(len(numList)):
        if numList[i] == None:
            numList[i] = numList[i-1]
    return numList

# print(numList)

print(fillInBlank(numList))

# for i in range(1,11):
#     print(i)