customerid = input("Enter Customer ID: ")

# typeof = isinstance(customerid, str)
# print(typeof)
if customerid.isnumeric():
    customeridi = int(customerid)

# elif customerid := int():
#    print('Invalid entry. Please enter numerical value.')

    if customeridi <= 100 and customeridi > 0:
        print('1st')

    elif customeridi > 100 and customeridi <= 250:
        print('2nd')

    elif customeridi > 250:
        print('All reservations taken.')

else :print('Please enter numerical value.')
