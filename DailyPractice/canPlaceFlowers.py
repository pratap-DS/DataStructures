import unittest
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # if len(flowerbed) < 3:
        #     if sum(flowerbed) == 0 and (n == 1 or n == 0):
        #         return True
        #     elif sum(flowerbed) >= 1 and n >= 1:
        #         return False
        #     elif sum(flowerbed) >= 1 and n == 0:
        #         return True

        # i,j,k = 0, 1, 2

        for z in range(len(flowerbed)):

            if ( z-1 < 0 or flowerbed[z-1] == 0) and flowerbed[z] == 0 and (z+1>len(flowerbed)-1 or flowerbed[z+1] == 0):

                flowerbed[z] = 1
                n -= 1

            if n == 0:
                return True

        return n <= 0



        

class TestCanPlaceFlowers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Input: flowerbed = [1, 0, 0, 0, 1], n = 1
        Output: True
        """
        self.assertEqual(self.solution.canPlaceFlowers([1, 0, 0, 0, 1], 1), True)

    def test_example_2(self):
        """
        Input: flowerbed = [1, 0, 0, 0, 1], n = 2
        Output: False
        """
        self.assertEqual(self.solution.canPlaceFlowers([1, 0, 0, 0, 1], 2), False)

    def test_zero_flowers_needed(self):
        """
        Input: flowerbed = [1, 0, 0, 0, 1], n = 0
        Output: True
        """
        self.assertEqual(self.solution.canPlaceFlowers([1, 0, 0, 0, 1], 0), True)

    def test_single_empty_plot(self):
        """
        Input: flowerbed = [0], n = 1
        Output: True
        """
        self.assertEqual(self.solution.canPlaceFlowers([0], 1), True)

    def test_single_occupied_plot(self):
        """
        Input: flowerbed = [1], n = 1
        Output: False
        """
        self.assertEqual(self.solution.canPlaceFlowers([1], 1), False)

    def test_start_boundary(self):
        """
        Input: flowerbed = [0, 0, 1, 0, 1], n = 1
        Output: True
        """
        self.assertEqual(self.solution.canPlaceFlowers([0, 0, 1, 0, 1], 1), True)

    def test_end_boundary(self):
        """
        Input: flowerbed = [1, 0, 0], n = 1
        Output: True
        """
        self.assertEqual(self.solution.canPlaceFlowers([1, 0, 0], 1), True)

    def test_all_empty(self):
        """
        Input: flowerbed = [0, 0, 0, 0, 0], n = 3
        Output: True
        """
        self.assertEqual(self.solution.canPlaceFlowers([0, 0, 0, 0, 0], 3), True)

    def test_large_n_impossible(self):
        """
        Input: flowerbed = [0, 0, 0, 0, 0], n = 4
        Output: False
        """
        self.assertEqual(self.solution.canPlaceFlowers([0, 0, 0, 0, 0], 4), False)

if __name__ == '__main__':
    unittest.main()