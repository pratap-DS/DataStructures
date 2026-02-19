import unittest

class Solution:
    def reverseVowels(self, s: str) -> str:
        # DO NOT IMPLEMENT
        ar = list(s)
        vowels='aeiouAEIOU'

        i,j = 0,len(ar)-1

        while(i<j):

            if ar[i] in vowels and ar[j] in vowels:

                ar[i], ar[j] = ar[j], ar[i]
                i += 1
                j -= 1

            if ar[i] not in vowels:
                i += 1

            if ar[j] not in vowels:
                j -= 1

        return "".join(ar)
 


class TestReverseVowels(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Input: s = "IceCreAm"
        Output: "AceCreIm"
        """
        self.assertEqual(self.solution.reverseVowels("IceCreAm"), "AceCreIm")

    def test_example_2(self):
        """
        Input: s = "leetcode"
        Output: "leotcede"
        """
        self.assertEqual(self.solution.reverseVowels("leetcode"), "leotcede")

    def test_no_vowels(self):
        """
        Input: s = "bcdfg"
        Output: "bcdfg"
        """
        self.assertEqual(self.solution.reverseVowels("bcdfg"), "bcdfg")

    def test_all_vowels(self):
        """
        Input: s = "aeiou"
        Output: "uoiea"
        """
        self.assertEqual(self.solution.reverseVowels("aeiou"), "uoiea")

    def test_mixed_case_vowels(self):
        """
        Input: s = "aA"
        Output: "Aa"
        """
        self.assertEqual(self.solution.reverseVowels("aA"), "Aa")

    def test_single_character_vowel(self):
        """
        Input: s = "U"
        Output: "U"
        """
        self.assertEqual(self.solution.reverseVowels("U"), "U")

    def test_single_character_consonant(self):
        """
        Input: s = "z"
        Output: "z"
        """
        self.assertEqual(self.solution.reverseVowels("z"), "z")

    def test_vowels_with_spaces_and_symbols(self):
        """
        Input: s = "a e!i"
        Output: "i e!a"
        """
        self.assertEqual(self.solution.reverseVowels("a e!i"), "i e!a")

if __name__ == '__main__':
    unittest.main()