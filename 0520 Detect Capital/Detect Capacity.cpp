class Solution {
public:
	bool detectCapitalUse(string word) {
		int count = 0;
		for (char tmp : word)
		{
			if (tmp <= 'Z')
				++count;
		}
		return count == 0 || count == word.size() || (count == 1 && word[0]>='A'&& word[0] <= 'Z');
	}
};