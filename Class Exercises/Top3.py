# Given a key/value structure, write a function that returns the top
# three players with the highest score, each being assigned with a medal.

# 8 or more players with score

scoreBoard = {
    'Jonathan': 100,
    'Jordan': 20,
    'Fiona': 40,
    'Matt': 60,
    'Carlos': 80 ,
    'Jorge': 30,
    'Jordan': 70,
    'An' :50,
    'Wes' :90,
    'Khanh' :10
    }

# sortedScore = [x for x in scoreBoard.values()]

# for x in range(0,10):
#     scoreBoard.values():list = x
#     sortedScore.append(x)

def scoreSort(scoreBoard:dict) ->list:
    sortedScore = sorted(scoreBoard, key=scoreBoard.get, reverse=True)

    print(sortedScore[0], 'Gold')
    print(sortedScore[1], 'Silver')
    print(sortedScore[2], 'Bronze')

scoreSort()
#     for score in scoreBoard.values():
#         sortedScore.append(score)
#         sortedScore.sort
#     return sortedScore


# print(sortedScore)

