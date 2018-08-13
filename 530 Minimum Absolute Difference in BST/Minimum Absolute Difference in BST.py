# -*- coding: utf-8 -*-

#########-------------############
'''
运用中序搜索实现BST有小到大排序
'''
#########-------------############

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.MS(root, res)
        print(res)
        return min(res[i] - res[i-1] for i in range(1,len(res)))
        
    def MS(self, root, res):
        if not root:
            return
        self.MS(root.left, res)
        res.append(root.val)
        self.MS(root.right, res)

