# Using python, make an API call to the random user api. Retrieve 10 users and 
# store the first and last name of each user you retrieve. Store the list of 
# users in alphabetical order by last name.

import requests
response = requests.get('https://random-data-api.com/api/v2/users?size=10').json()

lastNameList = []

# Loop userList 10 times

def getLastName():
    for lastName in response['last_name']:
        lastNameList.append(lastName)
        print(lastNameList)


getLastName()

# each time it loops, take last name and append it to a new list
# sort the new list ABCs


# Sort 




