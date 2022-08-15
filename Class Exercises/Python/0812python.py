from turtle import circle
import unittest

def rectangleArea(length, width): # Need length and width
    # Returns the value back to the caller
    return length * width

# Calc the area of circle
def circleArea(radius): # Need radius
    PI = 3.14
    return PI * radius**2

class TestAreas(unittest.TestCase):
    def testRectangleArea(self):
        self.assertEqual(rectangleArea(3,3),9)

    def testCircleArea(self):
        self.assertEqual(circleArea(5),78.5)

unittest.main()

# print(circleArea(2))
