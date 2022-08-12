# initializing lists
import itertools

letterSeat = ['A', 'B', 'C', 'D']
numberSeat = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

totalSeatingChart = list(itertools.product(letterSeat, numberSeat)) 
# print(totalSeatingChart)
# print(len(totalSeatingChart))

print (totalSeatingChart)


if numberSeat in list(totalSeatingChart):
    numberSeat.values == 1, 2
    print('First Class')