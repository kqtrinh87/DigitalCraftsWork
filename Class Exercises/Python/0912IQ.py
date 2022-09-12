# Given a file, write a function that swap all cases. 
# All uppercase letters should become lower case and vice versa. Write unit tests to confirm 
import unittest

file = open("C:/Users/kqtri/Documents/GitHub/DigitalCrafts/TextFiles/0912-1.txt", "r")
# file = open("C:/Users/kqtri/Documents/GitHub/DigitalCrafts/TextFiles/0912-2.txt", "r")
stringFile = str(file.read()) # Read the file and converts file into string
caseSwappedFile = (stringFile.swapcase()) # Swap cases in the string, save as a new variable for testing
print(caseSwappedFile)

# Need to createa a function, replace the text in the original file with caseswap changes


class TestConvertedCase(unittest.TestCase):
    def test_case(self):
        self.assertIsNot((file),caseSwappedFile) # Testing if they're not the same text (something changed) Not sure how to text if case changed
if __name__ == '__main__':
    unittest.main()

