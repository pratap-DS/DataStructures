# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:

    def build(self, preorder, upper, idx, l):

        print(idx, upper, preorder[idx])

        if idx == l or  preorder[idx] > upper:
            return None

        
        root = TreeNode(preorder[idx])
        # print(root.data)
        idx += 1

        root.left = self.build(preorder, root.data, idx,l)
        root.right = self.build(preorder, upper, idx,l)

        return root

    def bstFromPreorder(self, preorder):
        #your code goes here

        leng= len(preorder)

        return self.build(preorder, 10000, 0, leng)
    

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.data, end=" ")
            self.inorderTraversal(root.right)

# Main method for testing
if __name__ == "__main__":
    solution = Solution()
    preorder = [8, 5, 1, 7, 10, 12]

    root = solution.bstFromPreorder(preorder)

    # Print the constructed BST
    solution.inorderTraversal(root)

# testing

