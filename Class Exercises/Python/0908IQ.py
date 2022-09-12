# Create a program that generates 30 students. Each student should have an ID 
# and grade(numerical 0-100)
# Take those students grades and curve them, the highest grade becoming a 95. 
# Adjust your gradebook to assign a letter grade based on the new values
# Write a unittest to verify that your function is working

# Given a list of grades

# Curve them
# Assign letter grade
# print out

gradeBook = { ['id': 818979470, 'grade': 36], [id: 818979470, 'grade': 67], 
            ['id': 818979470, 'grade': 12']:, ['id': 818979470, 'grade': 12], 
            ['id': 818979470, 'grade': 88], ['id': 818979470, 'grade': 48], 
            ['id': 818979470, 'grade': 91], ['id': 818979470, 'grade': 46],
            ['id': 818979470, 'grade': 29], ['id': 818979470, 'grade'23]:,
            ['id': 818979470, 'grade': 70], ['id': 818979470, 'grade': 51] }

def curveGradeValue():
    for value in gradeBook.values(): # loop through the gradebook to see the highest grade
            if value < 95:
                highestGradeinGradeBook = max(gradeBook.values())
                curveAmount = (95 - highestGradeinGradeBook)
                print(curveAmount)

curveGradeValue()

# if grade is less than 95, curve by adding the difference of 95 minus the 
# highest grade.


# What if grades are above 95?
# convert grades above 100 to 100

