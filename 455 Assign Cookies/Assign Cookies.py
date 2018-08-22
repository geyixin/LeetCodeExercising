#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'geyixin'


class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        if s[0] >= g[-1]:
            return min(len(g), len(s))
        if s[-1] < g[0]:
            return 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i


# g = [1,2]
# s = [1,2,3]

# so = Solution()
# print(so.findContentChildren(g,s))