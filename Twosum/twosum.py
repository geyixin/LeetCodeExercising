#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'geyixin'

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lennums = len(nums)
        i = 0
        a = []
        while i < lennums-1:
            temp = target - nums[i]
            j = i + 1
            while j < lennums:
                if nums[j] == temp:
                    a.append(nums[i])
                    a.append(nums[j])
                j = j + 1
            i = i + 1
        return a


# nums = [2, 7, 11, 15]
# target = 17
# so = Solution()
# b = so.twoSum(nums, target)
# print(b)


