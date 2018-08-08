# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        temp = [root]
        while len(temp) > 0:
            nodes = temp.pop(0)
            res.append(nodes.val)
            for node in nodes.children[::-1]:
                temp.insert(0, node)
        return res

###########
# 输入：{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}
            #                 1

            #     3           2           4   

            # 5      6
# 1.如果把20行的pop(0)改成pop(),则输出：[1,4,2,3,6,5]
# 2.保留20行的pop(0)，把22行的children[::-1]改成children，也是输出：[1,4,2,3,6,5]
# 3.把把20行的pop(0)改成pop()，同时把22行的children[::-1]改成children，则输出：[1,3,2,4,5,6]
#########