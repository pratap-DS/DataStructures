import unittest, math
from typing import List

class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False

        firstSmallest = math.inf
        secondSmallest = math.inf
        firstIndex = -1
        secondIndex = -1

        for i in range(len(nums)):
            if nums[i] <= firstSmallest:
                firstSmallest = nums[i]
                firstIndex = i

            elif nums[i] <= secondSmallest:
                secondSmallest = nums[i]
                secondIndex = i
        
            else:
                return True

        return False







    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     i, j, k = 0, 1, 2
    #     n = len(nums)

    #     while(i < n-2 ):    #[1,5,0,4,1,3]

    #         if nums[i] < nums[j] < nums [k]:
    #             return True
    #         elif nums [i] < nums [j] > nums[k]:
    #             k += 1
    #         elif nums [i] > nums[j] < nums[k]:
    #             i += 1
    #             j += 1
    #             k += 1

    #         elif nums[i] > nums[j] > nums[k]:
    #             i += 1
    #             j += 1
    #             k += 1
    #         else:
    #             i += 1
    #             j += 1
    #             k += 1

    #         if k >= n:
    #             i = i+1
    #             j = i + 1
    #             k = j + 1


    #     return False

            
                






class TestIncreasingTriplet(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Input: nums = [1,5,0,4,1,3]
        Output: True
        """
        self.assertTrue(self.solution.increasingTriplet([1,5,0,4,1,3]))

    def test_example_2(self):
        """
        Input: nums = [5, 4, 3, 2, 1]
        Output: False
        """
        self.assertFalse(self.solution.increasingTriplet([5, 4, 3, 2, 1]))

    def test_example_3(self):
        """
        Input: nums = [2, 1, 5, 0, 4, 6]
        Output: True
        """
        self.assertTrue(self.solution.increasingTriplet([2, 1, 5, 0, 4, 6]))

    def test_small_length(self):
        """
        Input: nums = [1, 2]
        Output: False (Length must be at least 3)
        """
        self.assertFalse(self.solution.increasingTriplet([1, 2]))

    def test_with_duplicates(self):
        """
        Input: nums = [1, 1, 1, 1]
        Output: False (Strictly increasing required)
        """
        self.assertFalse(self.solution.increasingTriplet([1, 1, 1, 1]))

    def test_unsorted_with_triplet(self):
        """
        Input: nums = [20, 100, 10, 12, 5, 13]
        Output: True (10, 12, 13 is a valid triplet)
        """
        self.assertTrue(self.solution.increasingTriplet([20, 100, 10, 12, 5, 13]))

    def test_descending_with_jump(self):
        """
        Input: nums = [5, 1, 6]
        Output: False
        """
        self.assertFalse(self.solution.increasingTriplet([5, 1, 6]))

if __name__ == '__main__':
    unittest.main()