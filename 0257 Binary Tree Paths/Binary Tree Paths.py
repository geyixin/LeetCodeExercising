# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        oup, pp = [], []
        self.DFSMethod(root, pp, oup)
        return oup
    def DFSMethod(self, root, pp, oup):
        if not root:
            return None
        pp.append(str(root.val))
        #print(pp)
        if not root.left and not root.right:
            oup.append('->'.join(pp))
            #print(oup)
        if root.right:
            #print('right')
            self.DFSMethod(root.right, pp, oup)
        if root.left:
            #print('left')
            self.DFSMethod(root.left, pp, oup)
        pp.pop()