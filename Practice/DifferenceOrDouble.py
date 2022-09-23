# 4. In Python, given an int n, return the difference between n and 21, except return double the difference if n is over 21.

# # diff21(19) → 2
# # diff21(10) → 11
# # diff21(21) → 0

from random import randint

n = randint(0,100)
def diff21(n):
    if n > 21:
        print("Number: " + str(n) + " Double it into %d" % (2*n))
    if 0 < n <= 21:
        print("Number: " + str(n) + " Found the difference of %d" % (21-n))
diff21(n)
