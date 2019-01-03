"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        que = [(root, 0)]
        oup = [[]]
        while que:
            node, row = que.pop(0)
            if row >= len(oup):
                oup.append([])
            oup[row].append(node.val)
            for child in node.children:
                que.append((child, row + 1))
        return oup