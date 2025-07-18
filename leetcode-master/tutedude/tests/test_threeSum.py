import unittest
from src.threeSum import solve3Sum  # Make sure this import works

class TestThreeSum(unittest.TestCase):
    
    def test_no_result(self):
        myArr = [1, 2, 3, 4, 5]
        target = 9
        result = solve3Sum(myArr, target)
        self.assertEqual(result, [], "Expected no triplets summing to target")

if __name__ == '__main__':
    unittest.main()

