# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_Depth =  self.maxDepth(root.left)
        right_Depth =  self.maxDepth(root.right)
        return self.maxmax(left_Depth, right_Depth) + 1 
    def maxmax(self, a, b):
        if a > b :
            return a
        else:
            return b