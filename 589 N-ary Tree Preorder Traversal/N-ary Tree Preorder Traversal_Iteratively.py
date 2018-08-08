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