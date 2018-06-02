#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'geyixin'



class Solution:
    def threeSum(self, nums):
        lennums = len(nums)
        m = []
        nums.sort()
        i = 0
        while i < lennums - 2:
            j = i + 1
            p = lennums - 1
            while j < p:
                tem = nums[i]+nums[j]+nums[p]
                if tem == 0:
                    m.append([nums[i], nums[j], nums[p]])
                    j = j + 1
                    p = p - 1
                    while j < p:
                        if nums[j] != nums[j-1] or nums[p] != nums[p+1]:
                            break
                        j = j + 1
                        p = p - 1
                elif tem < 0:
                    j = j + 1
                else:
                    p = p - 1
            i = i + 1
            while i < lennums - 2:
                if nums[i] != nums[i-1]:
                    break
                i = i + 1
        return  m