import unittest
from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # ---------------------------------------------------------
        # TODO: Implement your logic here.
        # Set your breakpoint on the line below to start debugging!
        # ---------------------------------------------------------
        pass

def list_to_tree(items: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Constructs a binary tree from a list (LeetCode BFS style).
    Example: [1, 2, 3, None, None, 4, 5]
    """
    if not items:
        return None
    
    root = TreeNode(items[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(items):
        node = queue.popleft()
        
        # Build left child
        if i < len(items) and items[i] is not None:
            node.left = TreeNode(items[i])
            queue.append(node.left)
        i += 1
        
        # Build right child
        if i < len(items) and items[i] is not None:
            node.right = TreeNode(items[i])
            queue.append(node.right)
        i += 1
        
    return root

class TestSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        # p = [1,2,3], q = [1,2,3]
        p = list_to_tree([1, 2, 3])
        q = list_to_tree([1, 2, 3])
        self.assertTrue(self.solution.isSameTree(p, q))

    def test_case_2(self):
        # p = [1,2], q = [1,None,2]
        p = list_to_tree([1, 2])
        q = list_to_tree([1, None, 2])
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_case_3(self):
        # p = [1,2,1], q = [1,1,2]
        p = list_to_tree([1, 2, 1])
        q = list_to_tree([1, 1, 2])
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_case_4(self):
        # Both trees are empty
        p = list_to_tree([])
        q = list_to_tree([])
        self.assertTrue(self.solution.isSameTree(p, q))

if __name__ == "__main__":
    unittest.main()