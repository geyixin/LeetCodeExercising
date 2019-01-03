#!/usr/bin/env python
# -*- coding: utf-8 -*-

#####################-------------------#######################
'''
注意看两个LeftList()的定义和使用的差别
第三个是提交成功显示的速度最快的代码。
'''
#####################-------------  ----#######################



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ss = []
        self.LeftList(root, ss)

        return sum(ss)
        
    def LeftList(self, root, ss):
        if not root:
            return 0
        if root.left and self.IsLeaf(root.left):
            ss.append(root.left.val)
        self.LeftList(root.left, ss)
        self.LeftList(root.right, ss)

    def IsLeaf(self, root):
        if not root.left and not root.right:
            return True





# class Solution:
#     def sumOfLeftLeaves(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         res = self.LeftList(root)

#         return res
        
#     def LeftList(self, root):
#         if not root:
#             return 0
#         res = 0
#         if root.left and self.IsLeaf(root.left):
#             res += root.left.val
#         res = res + self.LeftList(root.left) + self.LeftList(root.right)
#         return res
        

#     def IsLeaf(self, root):
#         if not root.left and not root.right:
#             return True


# class Solution:
#     def sumOfLeftLeaves(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None:
#             return 0
#         sum = 0
#         if root.left is not None and root.left.left is None and root.left.right is None:
#             sum = root.left.val
        
#         return sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
