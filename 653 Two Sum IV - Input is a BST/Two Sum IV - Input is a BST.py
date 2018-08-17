#!/usr/bin/env python
# -*- coding:utf-8 -*-


######################-----------------------###################
"""
第一个是我自己所想，时间超级长，具体多少ms就不提了哈。
第二个是提交成功显示的时间最短的。
                                --让我静一静
"""
######################-----------------------###################


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = []
        
        def MS(root, res):
            if not root:
                return
            MS(root.left, res)
            res.append(root.val)
            MS(root.right, res)
        
        MS(root, res)
        
        return self.findHelper(res, k)
    
    def findHelper(self, res, k):
        if k >= 2*res[-1] or k <= 2*res[0]:
            return False
        LL = len(res)
        for i in range(LL):
            temp = k - res[i]
            j = LL -1
            while j > i:
                if temp == res[j]:
                    return True
                j -= 1
        return False

# class Solution:
#     def findTarget(self, root, k):
#         """
#         :type root: TreeNode
#         :type k: int
#         :rtype: bool
#         """
#         if not root:
#             return False
#         bfs, s = [root], set()
#         for i in bfs:
#             # print(i.val)
#             if k - i.val in s:
#                 return True
#             s.add(i.val)
#             if i.left:
#                 bfs.append(i.left)
#             if i.right:
#                 bfs.append(i.right)
#         return False