import unittest

class Solution:
    def reverseWords(self, s: str) -> str:

        sp = reversed(s.split())
        ar = [i for i in sp if i.isalnum]
        ans = " ".join(ar)
        return ans

class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Input: s = "the sky is blue"
        Output: "blue is sky the"
        """
        self.assertEqual(self.solution.reverseWords("the sky is blue"), "blue is sky the")

    def test_example_2(self):
        """
        Input: s = "  hello world  "
        Output: "world hello"
        """
        self.assertEqual(self.solution.reverseWords("  hello world  "), "world hello")

    def test_example_3(self):
        """
        Input: s = "a good   example"
        Output: "example good a"
        """
        self.assertEqual(self.solution.reverseWords("a good   example"), "example good a")

    def test_single_word(self):
        """
        Input: s = "word"
        Output: "word"
        """
        self.assertEqual(self.solution.reverseWords("word"), "word")

    def test_single_word_with_spaces(self):
        """
        Input: s = "   word   "
        Output: "word"
        """
        self.assertEqual(self.solution.reverseWords("   word   "), "word")

    def test_multiple_spaces_between_words(self):
        """
        Input: s = "this   is   a   test"
        Output: "test a is this"
        """
        self.assertEqual(self.solution.reverseWords("this   is   a   test"), "test a is this")

    def test_alphanumeric_words(self):
        """
        Input: s = "1st 2nd 3rd"
        Output: "3rd 2nd 1st"
        """
        self.assertEqual(self.solution.reverseWords("1st 2nd 3rd"), "3rd 2nd 1st")

if __name__ == '__main__':
    unittest.main()
