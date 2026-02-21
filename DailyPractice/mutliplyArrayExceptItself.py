import unittest
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        temp = 1
     
        ans = [temp]*n

        for i in range(0,n):
            ans[i] = temp
            temp *= nums[i]

        temp = 1

        for j in range(n-1,-1,-1):
            ans[j] *= temp
            temp *= nums[j]


        return ans

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Input: nums = [1, 2, 3, 4]
        Output: [24, 12, 8, 6]
        """
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_example_2(self):
        """
        Input: nums = [-1, 1, 0, -3, 3]
        Output: [0, 0, 9, 0, 0]
        """
        self.assertEqual(self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_all_positive(self):
        """
        Input: nums = [2, 3, 4, 5]
        Output: [60, 40, 30, 24]
        """
        self.assertEqual(self.solution.productExceptSelf([2, 3, 4, 5]), [60, 40, 30, 24])

    def test_with_multiple_zeros(self):
        """
        Input: nums = [0, 0, 1, 2]
        Output: [0, 0, 0, 0]
        """
        self.assertEqual(self.solution.productExceptSelf([0, 0, 1, 2]), [0, 0, 0, 0])

    def test_minimum_length(self):
        """
        Input: nums = [10, 20]
        Output: [20, 10]
        """
        self.assertEqual(self.solution.productExceptSelf([10, 20]), [20, 10])

    def test_negative_numbers(self):
        """
        Input: nums = [-1, -2, -3, -4]
        Output: [-24, -12, -8, -6]
        """
        self.assertEqual(self.solution.productExceptSelf([-1, -2, -3, -4]), [-24, -12, -8, -6])

if __name__ == '__main__':
    unittest.main()