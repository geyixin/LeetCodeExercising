class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ss = list(s)
        tt = list(t)
        for i in tt:
            if i in ss:
                ss.remove(i)
                continue
            else:
                return i