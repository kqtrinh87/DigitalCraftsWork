import itertools
import random

# class Flight:
#     def __init__(self):
    
#         self.happinessScore = 100
#         self.delayTime = 0
#         self.passengerDict = {
            
#         }
        
    def chanceOf(numOf, chance):    # calculates chances of something happening and return True or False
        randomNum = random.random() * 100
        randomNum = int(randomNum)
        if numOf * chance >= randomNum:
            return True
        else:
            return False
        
        row = range(1, 16)
        
    def populatePlane(self):
        numberSeat = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
        letterSeat = ['A', 'B', 'C', 'D']

        for x in numberSeat:
            for y in letterSeat:
                newInstance = First(x,y,80,50,1)
                self.passengerDict[x+y] = newInstance 
            
        print(self.passengerDict['1A'])



# totalSeatingChart = list(itertools.product(letterSeat, numberSeat)) 
# print(totalSeatingChart)


        #def kickFromPlane():
           
# class Passenger:
#     def __init__(self, row: str , seat: int, chanceOfReview: int, chanceOfRefusing: int, chanceOfPunching: int ):
#         self.row = row
#         self.seat = row        
#         self.chanceOfReview = chanceOfReview
#         self.chanceOfRefusing = chanceOfRefusing
#         self.chanceOfPunching = chanceOfPunching

        
#         def writeNegativereview():
#             chance = random.random() * 100
#                 if chance 
        
#         #def refuseToMove():
        
#         #def punchAttendent():


# class First(Passenger):
    
    
    
    
    

#class Business(Passenger):


# class ComfortPlus(Passenger):


# class Economy(Passenger):
    
#     def specialAbility():


# fancy = First('A', 1, 80, 50, 1)

# lowFancy = Business(range(3, 5), 70, 30, 2)

