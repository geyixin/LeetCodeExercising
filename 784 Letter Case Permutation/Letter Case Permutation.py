#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


###############-----------------#################
"""
第二个是提交成功看到的时间最短的代码
"""
###############-----------------#################


class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [S]

        for i in range(len(S)):
            temp = []
            for s in res:
                if s[i].isdigit():
                    temp.append(s)
                    continue
                temp.append(s[0:i] + s[i].lower() + s[i + 1:])
                temp.append(s[0:i] + s[i].upper() + s[i + 1:])
            res = temp
        return res

import itertools

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        string = []
        for s in S:
            if s.isalpha():
                string.append([s.upper(), s.lower()])
            else:
                string.append(s)
        # print(string)
        return [''.join(i) for i in itertools.product(*string)]

"""
当 s = "a1B2"  
print(string) :  [['A', 'a'], '1', ['B', 'b'], '2']
*string 等价于 string[0],string[1],string[2],string[3]
"""