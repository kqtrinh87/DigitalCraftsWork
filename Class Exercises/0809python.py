# Matrices
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(matrix[2] + matrix[1])

# for rows in range(len(matrix)):
#     # print(matrix[rows])
#     for cols in range(len(matrix[rows])):
#         print(matrix[rows][cols])

# # Print the matrix reverse
# for rows in range(len(matrix)-1,-1,-1):
#     # print(matrix[rows])
#     for cols in range(len(matrix[rows])-1,-1,-1):
#         print(matrix[rows][cols])

# Traverse the matrix in reverse using a while loop

#The original array
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# resarr = arr.reverse

# print("Before reversal Array is :",arr)
 
# arr.reverse() #reversing using reverse()
# print("After reversing Array:",arr)

import random
import useful

#Create the environment
#-----------------------------------------------------------

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
            print("It is raining! ")
            self.isRaining = True
        else:
            print("It is not raining. ")

    def treeLoss(self): # each woodchuck adds a 5% chance of lossing a tree
        numWoodchuck = self.woodchuck
        randomNum = random.random() * 100
        randomNum = int(randomNum)
        # print('The chance for losing a tree is ' + str(int(randomNum)) + '%')
        if numWoodchuck * 5 >= randomNum:
            print('A tree disappeared!')
            self.tree = self.tree - 1

    def treeGain(self):
        if self.waterlevel >= 100:
            self.tree = self.tree + 1 # changed self.tree to numTree -Khanh
            print("You have gain a tree. ")
            self.waterlevel = 0

# Run the game
#-----------------------------------------------------------
treeNum = useful.intput("Enter the amount of trees. ")
gnomeNum = useful.intput("Enter the amount of gnomes. ")
woodchuckNum = useful.intput("Enter the amount of woodchucks. ")
DcGarden = Garden(treeNum,gnomeNum,woodchuckNum)

DcGarden = Garden(4,5,2)
turn = 1

while turn <= 101:
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
    #print("")
    print("water level",DcGarden.waterlevel)
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