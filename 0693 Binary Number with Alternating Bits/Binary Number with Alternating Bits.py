class Solution:
    # 十进制转二进制
    # def int2b(self, n):
    #     b = '0'
    #     if n == 0:
    #         return b
    #     else:
    #         b = self.int2b(n//2)
    #         return b + str(n%2)
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # nn = self.int2b(n)[1:]
        # p = 0
        # ll = len(nn)-1
        # for i in range(ll):
        #     if nn[i] != nn[i+1]:
        #         p += 1
        #         continue
        #     else:
        #         break
        # return p==ll
        strn = bin(n)
        nn = strn.lstrip('0b')
        p = 0
        ll = len(nn)-1
        for i in range(ll):
            if nn[i] != nn[i+1]:
                p += 1
                continue
            else:
                break
        return p==ll
        