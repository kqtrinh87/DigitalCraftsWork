# the 2022 Hurricane season has been predicted to be above average. Write a
# simulation that spawns the hurricanes.  
# 1% cat5, 3% cat4, 6% cat3, 10% cat2, 12% cat1, 18% Tropical storm, 
# 20% Tropicial Depressions, 30% Nothing happens.
# Hurricane class should contain catgegory, destination, travel speed, and name.
# The constructor should handle the instantiation of all fields.
# Generate 25 events, storm or greater gets name, depression gets number

import random

class Storm:
    def __init__(self):
        self.category = ''
        self.destination = ''
        self.speed = 0
        self.name = ''
        self.assignCategory = ''

    stormList = ['Alex', 'Bonnie', 'Colin', 'Bonnie',
    'Danielle', 'Earl', 'Fiona', 'Gaston', 'Hermoine',
    'Idalia', 'Jose', 'Karl', 'Lisa', 'Martin', 'Nicole',
    'Owen', 'Phillippe', 'Rina', 'Shary', 'Tammy', 'Virginie',
    'Walter'] # Dictionary of Storm Names

    places = ['Honolulu', 'Miami', 'Atlanta', 'Charlotte',
    'Boston', 'New York', 'D.C.', 'Baltimore','Cape Hatteras',
    'Morehead', 'Wilmington', 'Savannah', 'Myrtle Beach']

    depressionCounter = 1
    stormCounter = 0

    def assignName(self):

    # def assignStatus(self):
    #     self.speed = random.randint(0,20)
    #     self.destination = self.places[random.randint(1,12)]
    #     self.name = self.stormList[self.stormCounter]
    #     self.stormCounter += 1

        def assignCategory(self):
            severity = random.randint(0,99)
            print(severity)
            if severity <= 70:
                print('Nothing happens.')
            elif severity >=49 and severity < 69:
                self.category = 'Tropical Depression'
                self.destination = self.places[random.randint(1,12)]
                self.speed = random.randint(0,20)
                self.name = self.stormList[self.stormCounter]
                self.stormCounter += 1
            elif severity >=20 and severity < 30:
                self.category = 'Category 1'
                self.speed = random.randint(0,20)
                self.name = self.stormList[self.stormCounter]
                self.stormCounter += 1
            elif severity >=20 and severity < 30:
                self.category = 'Category 1'
                self.speed = random.randint(0,20)
                self.name = self.stormList[self.stormCounter]
                self.stormCounter += 1
            elif severity >=20 and severity < 30:
                self.category = 'Category 1'
                self.speed = random.randint(0,20)
                self.name = self.stormList[self.stormCounter]
                self.stormCounter += 1
            elif severity >=20 and severity < 30:
                self.category = 'Category 1'
                self.speed = random.randint(0,20)
                self.name = self.stormList[self.stormCounter]
                self.stormCounter += 1

hurricane = Storm()
print(hurricane.category)
    # def chanceOfStorm():
    #     if  0 <= percentValue <= 1:
    #         stormNameSelect()
    #         print(nextStormName[0])
    #         nextStormName.clear


percentValue = (random.randint(0, 100))
# randomly pick a

# def pickName(stormNameDict):
#     for name in stormNameDict




# def cat5:
#     print(stormNameDict)



