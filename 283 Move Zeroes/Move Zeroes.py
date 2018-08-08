class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = [i for i in range(len(nums)) if nums[i] == 0]

        for j in range(len(temp)):
            nums.pop(temp[j])
            nums.append(0)
