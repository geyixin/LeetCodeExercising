# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        small = min(p.val, q.val)
        big = max(p.val, q.val)

        if small <= root.val <= big or not root:
            return root
        if big < root.val:
            # print('left')
            return self.lowestCommonAncestor(root.left, p, q)
        if small > root.val:
            # print('right')
            return self.lowestCommonAncestor(root.right, p, q)