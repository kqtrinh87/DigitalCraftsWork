import random

def intput(phrase: str) -> int:
    num = input(phrase)                     #gets input/num
    if str.isdigit(num) == True:            #checks if num is a num
        return int(num)
    while str.isdigit(num) == False:
        if str.isdigit(num[1:]) == True:    #checks if num is neg.
            return int(num) 
        else:                               #cycle again
            num = input("Try again. ")
            continue
    return int(num)

class Garden:
    def __init__(self, tree: int, gnome: int, woodchuck: int):
        self.tree = tree
        self.gnome = gnome
        self.woodchuck = woodchuck
        self.isRaining = False
        self.waterlevel = 0
        self.waterloss = 10
        self.waterlossConstant = 10

    def waterLoss(self):  # its shade decreases water loss by 2
        self.waterloss = 10

        if self.waterlevel - self.waterloss - (self.tree * 2) <= 0:
            self.waterlevel = 0
            # print("Water level has increased by %s! " % abs(self.waterloss)) #added increased by abs value
        else:
            self.waterloss = self.waterloss - (self.tree * 2)
            if self.waterloss < 0:
                self.waterlevel = self.waterlevel - self.waterloss
                print("Water level has decreased by %s! " % self.waterloss)

    def waterGain(self):
        self.waterlevel = self.waterlevel + 25

    def rainChance(self): # each instance adds a 5% chance of rain
        numGnome = self.gnome
        randomNum = random.random() * 100
        randomNum = int(randomNum)
        #print('The chance for rain is ' + str(int(randomNum)) + '%')
        if numGnome * 5 >= randomNum:
            print("It started to raining! ")
            self.isRaining = True
        else:
            print("Guess there's no rain today.")

    def treeLoss(self): # each woodchuck adds a 5% chance of lossing a tree
        numWoodchuck = self.woodchuck
        randomNum = random.random() * 100
        randomNum = int(randomNum)
        # print('The chance for losing a tree is ' + str(int(randomNum)) + '%')
        if numWoodchuck * 5 >= randomNum:
            print('A woodchuck destroyed a tree!')
            self.tree = self.tree - 1

    def treeGain(self):
        if self.waterlevel >= 100:
            self.tree = self.tree + 1 # changed self.tree to numTree -Khanh
            print("A tree has risen from the ground. ")
            self.waterlevel = 0

    def woodchuckGuest(self):
        randomNum = random.random() * 100
        randomNum = int(randomNum)
        if 5 >= randomNum:
            self.woodchuck += 1 
            print('A woodchuck has moved into your neighborhood!')
            
    def moreRain(self):
        randomNum = random.random() * 100
        randomNum = int(randomNum)
        if 5 >= randomNum:
            isRaining = True
            self.waterGain()
            print('Its a miracle! It has started to rain!')

# Run the game
#-----------------------------------------------------------
treeNum = intput("Enter the amount of trees. ")
gnomeNum = intput("Enter the amount of gnomes. ")
woodchuckNum = intput("Enter the amount of woodchucks. ")
DcGarden = Garden(treeNum,gnomeNum,woodchuckNum)

#DcGarden = Garden(4,5,2)

turn = 1
while DcGarden.tree < 11:
    DcGarden.isRaining = False
    print('Turn: #%d ' % turn)
    DcGarden.rainChance()
    if DcGarden.isRaining == True:
        DcGarden.waterGain()
        print("ran water gain. ")
    else:
        DcGarden.waterLoss()
    DcGarden.treeGain()
    DcGarden.treeLoss()
    DcGarden.woodchuckGuest()
    DcGarden.moreRain()
    #print("")
    print("Water level:",DcGarden.waterlevel)
    print('We have ' + str(int(DcGarden.tree)) + ' trees.')

    if DcGarden.tree == 10:
        print("You Won! ")
        break
    elif DcGarden.tree == 0:  #or DcGarden.waterlevel < 0:
        print("You Lost! ")
        break
    if turn % 10 == 0:
        randNum = random.randint(0,9)
        if randNum >= 5:
            print("You have gained a FREE tree! ")
            DcGarden.tree += 1
        elif randNum < 5:
            print("You have gained a FREE gnome! ")
            DcGarden.gnome += 1
    print("")
    
    turn += 1