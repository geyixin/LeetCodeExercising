class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LL = len(nums)
        Max1 = [0]
        for i in range(LL):
            Max1.append(self.dfs(nums, i, LL))

        return max(Max1)
        
    def dfs(self, nums, i, LL):
        if 0 <= i < LL and nums[i]:
            nums[i] = 0
            return 1 + self.dfs(nums, i-1, LL) + self.dfs(nums, i+1, LL)
        return 0