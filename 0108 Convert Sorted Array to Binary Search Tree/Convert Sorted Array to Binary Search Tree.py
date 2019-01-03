# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        numMid = len(nums)//2
        root = TreeNode(numMid)
        left = nums[:numMid]
        right = nums[numMid+1:]
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        return root