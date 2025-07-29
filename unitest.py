import unittest

# Function to be tested
def add(a, b):
    return a + b

# Unit test class
class TestAddFunction(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -4), -5)

#run the tests
unittest.main()
