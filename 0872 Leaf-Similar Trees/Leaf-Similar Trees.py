# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        r1 = []
        r2 = []
        self.leafFind(r1, root1)
        # print(r1)
        self.leafFind(r2, root2)
        # print(r2)
        return r1 == r2

    def leafFind(self, res, root):
        if root == None:
            return res
        if not root.left and not root.right:
            res.append(root.val)
        if root.left:
            self.leafFind(res, root.left)
        if root.right:
            self.leafFind(res, root.right)