# Create a class for car
# Create 2 child classes for electric vehicles and internal combustion
# engine vehicles
# All cars have curb weight, top speed, either all wheel drive or rear wheel
# drive, horsepower
# All cars can accelerate, brake, reverse. When accelerating print moving, when
# breaking print stopping, when reversing print backing up
# The electric vechile should have a battery capacity(kwH) and range
# Evs should have a function called charging that prints charging
# ICE vehicles should have MPG and a function refill

class Car:
    def __init__(self, curbWeight: int, topSpeed: int, horsepower: int, wheelDrive: str, ) -> None:
        self.curbWeight = curbWeight
        self.topSpeed = topSpeed
        self.horsepower = horsepower
        self.wheelDrive = wheelDrive
        

    def accelerate(self):
        print("The car is moving.")
    
    def brake(self):
        print("The car is stopping.")

    def reverse(self):
        print("The car is resversing.")
    
class Electrics(Car):
    def __init__(self, curbWeight: int, topSpeed: int, horsepower: int, wheelDrive: str, batteryCapacity: int, drivingRange: int) -> None:
        super().__init__(curbWeight, topSpeed, horsepower, wheelDrive)

        self.batteryCapacity = batteryCapacity
        self.drivingRange = drivingRange

    def evCharging(self):
        print("This EV is charging.")

class Combustions(Car):
    def __init__(self, curbWeight: int, topSpeed: int, horsepower: int, wheelDrive: str, milesPerGallon: int) -> None:
        super().__init__(curbWeight, topSpeed, horsepower, wheelDrive)

        self.milesPerGallon = milesPerGallon

    def refueling(self):
        print("This ICE vehicle is refueling.")

modelS = Electrics(4600, 216, 1000, 'All-Wheels Drive', 100, 400)
fit2011 = Combustions(2500, 120, 117, 'Rear-Wheels Drive', 34)

print('\nThis is the specs of the 2022 TELSA MODEL S:')
print("This car have a curb weight of %d lbs." % modelS.curbWeight)
print("This car have a top speed of %d mph." % modelS.topSpeed)
print("This car have a horsepower of %d hp." % modelS.horsepower)
print("This car is %s." % modelS.wheelDrive)
print("This car have a battery capacity of %d kwH." % modelS.batteryCapacity)
print("This car have a top range of %d miles." % modelS.drivingRange)
modelS.evCharging()

print('\nThis is the specs of the 2011 HONDA FIT:')
print("This car have a curb weight of %d lbs." % fit2011.curbWeight)
print("This car have a top speed of %d mph." % fit2011.topSpeed)
print("This car have a horsepower of %d hp." % fit2011.horsepower)
print("This car is %s." % fit2011.wheelDrive)
print("This car have a MPG of %d." % fit2011.milesPerGallon)
fit2011.refueling()


    