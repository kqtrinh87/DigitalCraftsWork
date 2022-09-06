# Given a list of users, ensure each user has a valid email, phone number, and zip code.
# Emailds must contain '@', phone numbers must have the format (xxx)-xxx-xxxx, and
# zip codes must be a valid US zip codes.
# from re import search

userDataInfo = list()
acceptedEmailDomain = '@gmail.com', '@yahoo.com', '@hotmail.com'
def collectInput():
    inputEmail = input("Enter your email adress:")
    userDataInfo.append(inputEmail)
    inputNumber = input("Enter your phone number:")
    userDataInfo.append(inputNumber)
    inputZipCode = input("Enter your zip code:")
    userDataInfo.append(inputZipCode)
    return userDataInfo
print("The list given as input by the user is :", userDataInfo)
    


def checkValidity(userDataInfo):
    if acceptedEmailDomain in userDataInfo:
        print('Correct!')
    else:
        print('Invalid Email Domain')

collectInput()
checkValidity()

# Incomplete



