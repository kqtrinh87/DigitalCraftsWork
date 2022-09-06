# There's a criminal on the loose! There's a been a raiad in your neighborhood and the suspect is at large. The GBI are searching
# for the suspect and know that the person of interest is within a 2 miles radius. Given a list of residences in the area
# write a function that determines which homes should be searched, and in what order based on the details provided. Return a list
# of addresses to be submitted to the GBI in their search.

susList = [{
    "name": "Bob",
    "distance": 1.2,
    "crimes_committed": 1,
    "address": "4325 Birch St"
},
{
    "name": "May",
    "distance": 0.3,
    "crimes_committed": 3,
    "address": "8903 Trolley St"
},
{
    "name": "Tyler",
    "distance": 0.8,
    "crimes_committed": 0,
    "address": "2348 Magnolia Dr"
},
{
    "name": "Reggie",
    "distance": 0.5,
    "crimes_committed": 1,
    "address": "3478 Seminole Ln"
},
{
    "name": "Seth",
    "distance": 3.2,
    "crimes_committed": 0,
    "address": "9803 Azul St"
},
{
    "name": "Ray",
    "distance": 2.9,
    "crimes_committed": 0,
    "address": "3467 Frost St"
},
{
    "name": "Kim",
    "distance": 0.1,
    "crimes_committed": 0,
    "address": "7893 Daisy Ln"
},
{
    "name": "Lisa",
    "distance": 1.2,
    "crimes_committed": 1,
    "address": "2345 Gale St"
},
{
    "name": "Ashley",
    "distance": 1.5,
    "crimes_committed": 5,
    "address": "6783 Sycamore St"
},
{
    "name": "Turner",
    "distance": 4.3,
    "crimes_committed": 1,
    "address": "8923 Pecan Ln"
},
]

# susListWithin2miles = []
# susListOver2miles = []

# def search2milesradius():
#     for suspect in susList:
#         if suspect["distance"] <= 2:
#             susListWithin2miles.append(susList)
#         else:
#             susListOver2miles.append(susList)

# search2milesradius()

for prep in susList:
    # Use bubblesort to arrange addresses from least distance or greatest
    for i in range(len(susList)):
        for currentIndex in range(0,len(susList)-i-1):
            if prep.get('distance') > prep[currentIndex +1]:
                prep[currentIndex], prep[currentIndex +1] = prep[currentIndex +1], prep[currentIndex]
    print(susList)
    # if prep.get('distance') < 2:
    #     for 
    #     print(prep)









