# Given the list of numbers, write a function that tallies the number even and
# odds occourences and return the results.
#Write a unit test to prove your function works

import unittest


numList = [3, 564, 44, 65, 52, 2, 7]
evenList = []
oddList = []

def evenOrOdds(numList):
    for num in numList:
        if num % 2 == 0:
            evenList.append(num)
        else:
            oddList.append(num)

evenOrOdds(numList)

print (len(evenList))
print("There are %d even numbers in given list. They're " % len(evenList))
print(evenList)
print("There are %d odd numbers in given list. They're " % len(oddList))
print(oddList)

class TestNums(unittest.TestCase):
    def testEvenOrOdds(self):
        self.assertEqual(len(evenList) == 4)
        self.assertEqual(len(oddList) == 3)

if __name__ == '__main__':
   unittest.main()

