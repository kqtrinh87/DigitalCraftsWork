# Functions: is a reusable block that can be called at
# any time

# "def" - User will pass in a name as a parameters, and
# the computer will say "Hey, name_of_user"

# A parameter is a variable that a function takes in

# userName = input('What is your name?: ')

# # userName is a parameter, the computer is taking the argument
# # that was passed in by the function
# # caller and storing that value in a variable userName
# def sayHey(userName):
#     print('Hey ': userName)

# # 'name' here is an argument
# sayHey(name)

# Calc the area of rectangle

# def rectangleArea(length, width): # Need len and wid
#     # Returns the value back to the caller
#     return length * width
# area_of_rectangle = rectangleArea(5, 6)
# print(area_of_rectangle)

# # Calc the area of circle
# def circleArea(radius): # Need radius
#     PI = 3.14
#     return PI * radius**2

# print(circleArea(2))

# # Should I wear a sweater?

# def wearSweater():
#     temperature = int(input("What's the current temperature outside?: "))
#     humidity = int(input("What is the current humidity outside?: "))
#     windSpeed = int(input("What is the current wind speed outside?: "))

#     wearSweater = False

#     if temperature < 55:
#         wearSweater = True
#     elif temperature >= 55 and temperature < 65 and humidity < 30:
#         wearSweater = True
#     elif temperature < 60 and windSpeed > 10:
#         wearSweater = True

#     return wearSweater

# print(wearSweater())

# There's two Type langauges (Strong Type and Not Strong Type)

# def rectangleArea(length: int, width: int) -> int: # '->' means returns
#     # Returns the value back to the caller
#     return length * width
# area_of_rectangle = rectangleArea(5, 6)
# print(area_of_rectangle)


# # Function to calc how much flooring to order calling the
# # previous function rectangleArea above.
# def orderFlooring(orderNumber: int, length: int, width: int) -> int:
#     if orderNumber <= 0:
#         print("Invalid Order Number.")
#     amount_of_flooring = rectangleArea(length, width)
#     return amount_of_flooring

# # You ordered x sq. ft of flooring.
# print(orderFlooring(101, 20, 15))


# EXTRA: Recursion "Like a loop"

# def doubleNumber(number: int) -> int:
#     doubleNumber(number * 2)

#------------------------------------------------------------------------------

# Dictionary: a list of key value pairs

# student0 = {
#     "id": 1234567,
#     "name": "Khanh Trinh",
#     "class": "Senior",
#     "GPA":  3.87
# }
# print(student0["id"])

# student1 = {
#     "id": 2345678,
#     "name": "wes Fountain",
#     "class": "Senior",
#     "GPA":  4.15
# }
# student2 = {
#     "id": 3456789,
#     "name": "An Nguyen",
#     "class": "Senior",
#     "GPA":  4.25

# }
# student3 = {
#     "id": 4567890,
#     "name": "Matt",
#     "class": "Senior",
#     "GPA":  3.89

# }
# student4 = {
#     "id": 5678901,
#     "name": "Jordan Boardman",
#     "class": "Senior",
#     "GPA":  4.26

# }
# student5 = {
#     "id": 6789012,
#     "name": "Fiona Eckert",
#     "class": "Senior",
#     "GPA":  4.48

# }
# student6 = {
#     "id": 7890123,
#     "name": "Jonathan",
#     "class": "Senior",
#     "GPA":  4.09

# }
# dcClass = [student0, student1, student2]
# print(dcClass)

# # Pull the dcClass, index 1 then pull "name"
# print(dcClass[1]["name"])

# Create a function using the class list above, return a list
# that contains the student bio of any student whose id is
# less than a number

# print()

# Given the list above, write a function that sorts the student in the class
# based on their id, and returns that list

student = {
    "id": 790283,
    "name": "Dre Taylor",
    "class": "Senior",
    "GPA": 3.87
}

#print(student["GPA"])


student1 = {
    "id": "478923",
    "name": "Wes Fountain",
    "bootcamp": "Digitalcrafts"
}


student2 = {
    "id": "578490",
    "name": "Jorge Rodriguez",
    "bootcamp": "Digitalcrafts"
}

student3 = {
    "id": "453789",
    "name": "Khanh Trinh",
    "bootcamp": "Digitalcrafts"
}

student4 = {
    "id": "945890",
    "name": "Jonathan",
    "bootcamp": "Digitalcrafts"
}

student5 = {
    "id": "578909",
    "name": "Fiona Eckert",
    "bootcamp": "Digitalcrafts"
}

# Given the list above, write a function that sorts the students in the class based on their id, and returns that list

# List of dictionaries
digitalcrafts_class = [student1, student2, student3, student4, student5]
# print(digitalcrafts_class)

# def listSort(oldList: list) -> list:
#     newList = []
#     topNumber = 0 
#     for x in oldList:
#         idNum = int(x["id"])
#         print(idNum)
#         if idNum > topNumber:
#             topNumber = idNum
#             newList.append(x)
        
#         elif idNum < topNumber:
#             i = 0
#             print(len(newList))
#             while i < 5:
#                 print('Index: ', i)
#                 newIdNum = int(newList[i]["id"])
#                 if idNum < newIdNum:
#                     newList.insert(i, x)
#                 i += 1
#     print(newList)

# listSort(digitalcrafts_class)

# From Stack Overflow

# import operator
# print(digitalcrafts_class.sort(key=operator.itemgetter("id")))

# Fiona E. Solution
def listSort(oldList:list) ->list:
    sortedList = []
    for students in oldList:
        sortedList.append(students["id"])
        sortedList.sort
    return sortedList
listSort(digitalcrafts_class)

print(listSort(digitalcrafts_class))