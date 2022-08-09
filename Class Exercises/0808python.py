# Functions are used to make your modular
# Whenever we call a function we type in the name exampleFunction(....)
# Parameters are values that a function recieves. These parameters are variables
# that are created and can only be used within the scope of the function. 

# def whatsTheDate(date: str) -> str:
#     return "Today's date is: %s" % date

# # Functions die after its complete
# whatsTheDate(8)

# # Functions can call other functions
# def whatsTheMonth(month: str):
#     return 'We are in the month of: %s \n' % month
    
#     # Calling the pervious function to print the date
#     print(whatsTheDate(8))

# whatsTheMonth('August')

# def dateTeller(month: str, date: str, year:str ) -> str:
#     print(whatsTheMonth(month) + whatsTheDate(date) + year)

# dateTeller('August', '8', '2022')

#-----------------------------------------------------------------------
# Tuples
# Can store  multiple values to one variable. Not mutable, meaning values cannot
# be changed after instaniation. Similiar to list or arrays

# my_favorite_colors = ('blue', 'purple')
# print(type(my_favorite_colors))

# -----------------------------------------------------------------------

# userInput0 = input("Type in whatever and watch it be typed backward!: ")
# def userInput1(x):
#   return x[::-1]

# inputreversed = userInput1(userInput0)

# print(inputreversed)

#-----------------------------------------------------------------------
# Slicing
# Changes the way we iterate over a string or list/array
# The first number represents the index we are starting at
# The second number is going to be the index we end at
# The last number dictates how many numbers to skip by

# Lets get the odd numbers from a string 
# numbers = '1234567890'
# print(numbers[0:9:2])
# It starts at index 0, ends at index 9, go by 2

# Lets get the even numbers
# print(numbers[1:9:2])
# It starts at index 1, ends at index 9, go by 2

# Now Get the prime numbers in reserve order
# Prime number is a number that is greater than 1 and is only divisble by 1 and itself
# 2, 3, 5, 7

# reverseOrder = numbers[::-1]
# primeNumbers = []
# for x in reverseOrder:
#     if int(x) % 2 != 0 and int(x) > 1:
#         primeNumbers.append(int(x))
# # elif reverseOrder (Finish this for homework)
# print(primeNumbers)

# # Lets finish this for homework practice, An provided the foundation,
# # now lets get the edge case

# print(numbers[9:3:-2])

#----------------------------------------------------------------------
# Object Oriented Programming
# Class is a definite of an object

# How to define a class; class names are typically uppercase
class Pokemon:
    # Constructor: they defines the bare minimum to create an object
    def __init__(self, hitPoints: int, pokeName: str, type: tuple, weakness: tuple):
        __hitPoints = 0
        self.hp = hitPoints
        self.name = pokeName
        self.type = type
        self.weakness = weakness
        self.damage = 0
        self.status = {
            'Frozen':False,
            'Burnt': False,
            'Poisoned': False,
            'Paraylzed': False
        }
    def __run(self):
        print('You fled the battle.')

    def useItem(self, item):
        print('You used the %s' % item)


Pikachu = Pokemon(40, 'Pikachu', 'electric', 'ground')
print(Pikachu.hp)

Squirtle = Pokemon(50, 'Squirtle', 'electric', ('grass, electric'))
print(Squirtle.weakness)

Squirtle.run()
Pikachu.run()

Pikachu.useItem('potion')

Blaziken = Pokemon(120, 'Blaziken', ('fire', 'fighting'), ('water', 'psychic'))
print(Blaziken.type[1])

# Inheritance
# When a child class, takes on the properties of a parent class,
# we call that inheritance
# Since Pikachu 
class Pikachu(Pokemon):
    def thunderbolt(self):
        print('%s used Thunderbolt!' % self.name)
        damage = 50
    def quickAttack(self, name):
        print('%s used quick attack!' % name)
        damage = 30
    def useItem(self, item):
        print("You used the %s. % item")
        print("It's still Pikachu's turn, select a move!")
    
    def heal(self, hp):
        self.hp +=100

    # using setters to update a Pokeman's HP
    def setHp(self, hp):
        if hp > 100:
            return 'Error: Cannot heal potion by that amount.'
        else:
            self.hp += hp


class Electrabuzz(Pokemon):
    def thunderbolt(self):
        damage = 80

Raichu = Pikachu(100, 'Raichu', ('electric'), ('ground'))
Raichu.thunderbolt()

Pikachu.run()

# Create a Cat/Dog game, create a class for both the cat and dog. Both animals
# should have the following properties: breed, weight, fur color, name
# Each animal will make their own unique sound
# Cat/Dog class which can do everything that both animals can do, but in its
# unique twist

