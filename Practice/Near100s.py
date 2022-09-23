# 5. In Python, given an int n, return True if it is within 10 of 100 or 200. 

# # near_hundred(93) → True
# # near_hundred(90) → True
# # near_hundred(89) → False

from random import randint

n = randint(0,300) # Given a random integer. Given a range of 0 thru 300.
if n >= 90 and n <= 110: # If that number is greater than or equal to 90 and less than or equal to 110. Return True with that number.
    print("True. %d is within 10 of 100" % (n))
elif n >= 190 and n <= 210: # If that number is greater than or equal to 190 and less than or equal to 210. Return True with that number.
    print("True. %d is within 10 of 200" % (n))
else: # If that number doesn't fall in either arguement, return False with that number.
    print("False. %d is not within 10 of 100 or 200." % (n))

