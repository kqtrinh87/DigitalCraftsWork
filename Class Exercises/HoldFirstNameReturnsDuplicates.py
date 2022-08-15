
studentRoster = ['Jonathan', 'Jordan', 'Fiona', 'Matt', 'Carlos', 'Jorge', 'Jordan', 'An', 'Wes', 'Khanh']

# sDict1 = {}
# sDict2 = {}

# def check1 ():
#     dict1 = checkDup(sDict1)
#     dict2 = checkDup(sDict2)
# print(sDict2)

def checkDup(studentRoster: list) -> dict:
    rosterDict = {}
    for name in studentRoster:
        if name in rosterDict.keys():
            rosterDict[name] = rosterDict.get(name) + 1
        else:
            rosterDict[name] = 1
        
        return rosterDict

    print(checkDup(studentRoster))

