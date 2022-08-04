customerid = input("Enter Customer ID: ")

if customerid.isnumeric():
    customeridi = int(customerid)

# Haven't resolve the case where input is 0
    if customeridi <= 100 and customeridi > 0:
        print('1st')

    elif customeridi > 100 and customeridi <= 250:
        print('2nd')

    elif customeridi > 250:
        print('All reservations taken.')

else :print('Invalid entry. Please enter numerical value.')
