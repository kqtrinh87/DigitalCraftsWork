# Write a short program that prints each number from 1 to 100 on a new line. 

# For each multiple of 3, print "Fizz" instead of the number. 

# For each multiple of 5, print "Buzz" instead of the number. 

# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.


# for startnum in range(1, 101):
#     if startnum % 3 == 0 and startnum % 5 != 0:
#         print('Fizz')
#     elif startnum % 5 == 0 and startnum % 3 != 0:
#         print('Buzz')
#     elif startnum % 5 == 0 and startnum % 3 == 0:
#         print('FizzBuzz')
#     else:
#         print(startnum)

# Reserving a string or list

name = "Khanh Trinh"
list = ['Khanh', 'Matt', 'Jordan', 'Matt']

print(name)
print(name[::-1])

# i = len(list)-1
# listB=[]
# while i >=0:
#     listB.append(list[i])
#     i = i-1
# print(listB)

ordinalList = ['1st', '2nd', '3rd']
reversedOrdinalList = []
while len(ordinalList) > 0:
    ordinal = ordinalList.pop()
    reversedOrdinalList.append(ordinal)
print(reversedOrdinalList)