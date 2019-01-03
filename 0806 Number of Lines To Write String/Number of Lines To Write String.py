class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        zimu = ['a','b','c','d','e','f','g','h','i',
                'j','k','l','m','n','o','p','q','r',
                's','t','u','v','w','x','y','z']
        dicTT = dict.fromkeys(zimu, 0)
        for i in range(26):
            dicTT[zimu[i]] = widths[i]
        changdu = 0
        if S:
            hangshu = 1
            for i in range(len(S)):
                # print(S[i], dicTT[S[i]], widths[dicTT[S[i]]])
                temp = dicTT[S[i]]
                changdu += temp
                # print('temp, changdu',temp, changdu)
                if changdu > 100:
                    changdu = temp
                    hangshu += 1
        else:
            hangshu = 0

        return [hangshu, changdu]