#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################------------------------###################
'''
第一个是我自己做的，慢如蜗牛，80ms；
第二个是提交成功看到的最快的，36ms。

			--不想说话，贴出来对比
			   感觉脸很疼！！！
'''

########################------------------------###################


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        b = sorted(nums)
        LL = len(nums)
        for i in range(LL):
            temp = target - b[i]
            j = LL -1
            while j > i:
                if temp == b[j]:
                    for ii, e in enumerate(nums):
                    	if len(a) == 2:
                            return a
                        if e == b[i]:
                            a.append(ii)
                            continue
                        if e == b[j]:
                            a.append(ii)
                            continue
                j -= 1
        return a


# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dic = {}
#         for i, num in enumerate(nums):
#             if (target - num) in dic:
#                 return i,dic[target - num]
#             dic[num] = i