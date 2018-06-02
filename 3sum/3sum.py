#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'geyixin'



class Solution:
    def threeSum(self, nums):
        n = len(nums)
        m = []
        for i in range(n-2):
            for j in range(i+1, n-1):
                for p in range(j+1, n):
                    if (nums[i]+nums[j]+nums[p]) == 0:
                        m.append([nums[i], nums[j], nums[p]])
        for k in range(len(m)-1):
            if len(m[k]) != 0:
                for t in range(k+1, len(m)):
                    if len(m[t]) != 0:
                        if set(m[t]) == set(m[k]):
                            m[t] = []
        while [] in m:
            m.remove([])
        return m