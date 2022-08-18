#  An animal rescue center in Atlanta in overcrowded and needs to send some 
# of their dogs to nearly locations. They will be sending any dogs with
# brown fur or that weighs over 50 lbs. to the new shelter. Write a function
# that returns the current allocation of dogs at each center.
# Ex: 
#   breed: German Shepard, weight 88 lbs., fur: brown, black
#   breed: Golden Retriever, weight 45 lbs., fur: tan
#   breed: Terrier, weight 29 lbs., fur black
#   breed: French Bulldog, weight 12 lbs., fur gray
#   breed: Beagle, weight 22 lbs, fur: brown, white, black
#   breed: Poodle, weight 62 lbs, fur: brown


Gray = {
    "Breed": "German Sephard",
    "Weight": 88,
    "Fur" : ["Brown", "Black"]
}
Jenny = {
    "Breed": "Golden Retriever",
    "Weight": 45,
    "Fur" : ["Tan"]
}
Timmy = {
    "Breed": "Terrier",
    "Weight": 29,
    "Fur" : ["Black"]
}
Frankie = {
    "Breed": "French Bulldog",
    "Weight": 22,
    "Fur" : ["Brown", "White", "Black"]
}
Benny = {
    "Breed": "Beagle",
    "Weight": 45,
    "Fur" : ["Tan"]
}
Penny = {
    "Breed": "Poodle",
    "Weight": 62,
    "Fur" : ["White"]
}
totalList = [Gray, Jenny, Timmy, Frankie, Benny, Penny]

def moveDogs(totalList):
    for dogs in totalList:
        if dogs['Weight'] > 50 or dogs['Fur'] == 'Brown':
            newCenter.append(dogs)
        else:
            oldCenter.append(dogs)

oldCenter = []
newCenter = []

print('The old shelter will keep the following dogs:' + str(oldCenter))

print('\nThe new shelter will have the following dogs:' + str(newCenter))

