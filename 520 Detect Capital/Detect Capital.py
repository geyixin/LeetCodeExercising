class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        low = word.lower()
        upp = word.upper()
        if upp == word or low == word:
            return True
        elif word[0] == upp[0] and low[1:] == word[1:]:
                return True
        else:
            return False