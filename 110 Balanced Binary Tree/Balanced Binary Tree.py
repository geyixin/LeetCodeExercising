# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        L = self.height(root.left)
        R = self.height(root.right)
        if abs(L - R) > 1:
            return False
        else:
            return self.isBalanced(root.left) and  self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0
        L = self.height(root.left)
        R = self.height(root.right)
        return max(L, R) + 1
        