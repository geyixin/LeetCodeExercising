class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        keys = [5, 10, 20]
        dd = dict.fromkeys(keys[:2], 0)
        for i in range(len(bills)):
            if bills[i] == keys[0]:
                dd[keys[0]] += 1

            elif bills[i] == keys[1]:
                dd[keys[1]] += 1
                if dd[keys[0]] > 0:
                    dd[keys[0]] -= 1
                else:
                    return False
            else:
                if dd[keys[0]] > 0 and dd[keys[1]] > 0:
                    dd[keys[0]] -= 1
                    dd[keys[1]] -= 1
                elif dd[keys[0]] >= 3:
                    dd[keys[0]] -= 3
                else:
                    return False
        return True