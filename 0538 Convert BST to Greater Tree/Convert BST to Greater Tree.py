# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = [0]
        self.MS(root, res)
        return root
    def MS(self, root, res):
        if not root:
            return 0
        self.MS(root.right, res)
        root.val += res[-1]
        res.append(root.val)        
        self.MS(root.left, res)