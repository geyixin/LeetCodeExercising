# -*- coding: utf-8 -*-

###########--------------------------------------#############
'''
第一个是本人的，
第二个是代码通过之后，在通过页面看到的。
感觉被深深的打脸了，哎！！

				--总结：换个方向，风景截然不同
'''
###########--------------------------------------#############

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        Gain = 0
        Temp = True
        LL = len(prices)
        for i in range(LL-1):
            if prices[i] <= prices[i+1]:
                if Temp:
                    Gain = 0 - prices[i] + Gain
                    Temp = False
                if i == LL-2:
                    Gain += prices[-1]
                    return Gain
            if prices[i] > prices[i+1]:
                if not Temp:
                    Gain += prices[i]
                Temp = True

        return Gain


# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         ans = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i - 1]:
#                 ans += prices[i] - prices[i - 1]
#         return ans