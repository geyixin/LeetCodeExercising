class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max1 = 0
        p = 0
        for num in nums:
            if num == 1:
                p += 1
            if num == 0:
                Max1 = max(Max1, p)
                p = 0

        return max(Max1, p)