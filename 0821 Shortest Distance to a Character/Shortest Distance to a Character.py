class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        CC = []
        ouP = []
        for i, v in enumerate(S):
            if v == C:
                CC.append(i)
        for i, v in enumerate(S):
            temp = []
            for j in CC:
                temp.append(abs(i-j))
            temp.sort()
            ouP.append(temp[0])
            # ouP.append(min(temp))

        return ouP