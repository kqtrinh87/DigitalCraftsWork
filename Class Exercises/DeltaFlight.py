import random

class Flight:
    def __init__(self):
        
        self.peopleToKick = 6
        self.happinessScore = 100
        self.delayTime = 0
        self.firstClass = First()
        self.businessClass = Business()
        self.comfortPlusClass = ComfortPlus()
        self.economyClass = Economy()

    def kickPassenger(self, classLetter: str):
        
        if classLetter == 'F':
            randomNum = random.randint(1,3) # random.choice
            if randomNum == 1:
                self.happinessScore += self.firstClass.checkIfReview()
            elif randomNum == 2:
                self.delayTime += self.firstClass.checkIfRefuse()
            elif randomNum == 3: 
                self.happinessScore += self.firstClass.checkIfPunch()

        elif classLetter == 'B':
            randomNum = random.randint(1,3)
            if randomNum == 1:
                self.happinessScore += self.businessClass.checkIfReview()
            elif randomNum == 2:
                self.delayTime += self.businessClass.checkIfRefuse()
            elif randomNum == 3: 
                self.happinessScore += self.businessClass.checkIfPunch()
        
        elif classLetter == 'C':
            randomNum = random.randint(1,3)
            if randomNum == 1:
                self.happinessScore += self.comfortPlusClass.checkIfReview()
            elif randomNum == 2:
                self.delayTime += self.comfortPlusClass.checkIfRefuse()
            elif randomNum == 3: 
                self.happinessScore += self.comfortPlusClass.checkIfPunch()
        
        elif classLetter == 'E':
            randomNum = random.randint(1,4)
            if randomNum == 1:
                self.happinessScore += self.economyClass.checkIfReview()
            elif randomNum == 2:
                self.delayTime += self.economyClass.checkIfRefuse()
            elif randomNum == 3: 
                self.happinessScore += self.economyClass.checkIfPunch()
            elif randomNum == 4:
                self.happinessScore += self.economyClass.specialAbility()
    
    def ifDelayed(self):
        if self.delayTime != 0 and self.delayTime % 30 == 0:
            self.happinessScore  -= 3

class Passenger:

    def checkIfReview(self) -> int:
        chance = random.random() * 100 
        if chance < self.chanceOfReview:
            print('A negative review has been written! Happiness went down by 1.')
            return -1
        else:
            return 0

    def checkIfRefuse(self) -> int:
        chance = random.random() * 100
        if chance < self.chanceOfRefusing:
            print('A passenger refused to move! The flight was delayed by 5 minutes.')
            return 5
        else:
            return 0
            
    def checkIfPunch(self) -> int:
        chance = random.random() * 100
        if chance < self.chanceOfPunching:
            print('A flight attendent has been punched!  Happiness went down by 10.')
            return -10
        else:
            return 0

class First(Passenger):
    def __init__(self):
        self.chanceOfReview = 80
        self.chanceOfRefusing = 50
        self.chanceOfPunching = 1
    
class Business(Passenger):
    def __init__(self):
        self.chanceOfReview = 70
        self.chanceOfRefusing = 30
        self.chanceOfPunching = 2


class ComfortPlus(Passenger):
    def __init__(self):
        self.chanceOfReview = 50
        self.chanceOfRefusing = 20
        self.chanceOfPunching = 5

class Economy(Passenger):
    def __init__(self):
        self.chanceOfReview = 10
        self.chanceOfRefusing = 10
        self.chanceOfPunching = 15
        self.chanceOfSpecial = 90
    
    def specialAbility(self):
        chance = random.random() * 100
        if chance < self.chanceOfSpecial:
            print("Someone Chuck Norris'd the flight attendant!! The whole flight is cancelled!")
            return -100
        else:
            return 0


flight = Flight()

while flight.peopleToKick > 0:
    print('\n\nNum of people left to kick: ' , flight.peopleToKick)
    classToKick = input('Choose class to kick: F for First Class, B for Business, C for Comfort+, E for Economy: ')
    
    flight.kickPassenger(classToKick)
    flight.ifDelayed()
    print('Happiness Score: ', flight.happinessScore)
    print('Delayed Time: %i minutes' % flight.delayTime)

    if classToKick == 'F' or classToKick == 'B' or classToKick == 'C' or classToKick == 'E':
        flight.peopleToKick -= 1

    if flight.peopleToKick == 0 and flight.happinessScore >= 70:
        print ('You win.')
    elif flight.peopleToKick == 0 and flight.happinessScore < 70:
        print ('You lose.')
        break