# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return 0 == 0
        if p == None and q != None or p != None and q == None or p.val != q.val:
            return 0 == 1
        else:
            r = self.isSameTree(p.right, q.right)
            l = self.isSameTree(p.left, q.left)
            return r and l
