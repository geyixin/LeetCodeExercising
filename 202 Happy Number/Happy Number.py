#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        Loop = set()  # 防止死循环

        def pw(n):
            res = 0
            while n > 0:
                res += (n%10)**2
                n //= 10
            return res
        
        while n != 1 and n not in Loop:
            Loop.add(n)
            n = pw(n)
            
        return n == 1