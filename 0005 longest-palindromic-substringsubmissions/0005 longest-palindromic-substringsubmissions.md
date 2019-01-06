# 5 longest-palindromic-substringsubmissions(最长回文子串)

+ [题目链接](https://leetcode-cn.com/problems/longest-palindromic-substring/)

+ 方法1：中心扩展算法

+ 以第i个节点为水波的中心点，然后向字符串的两端扩散，当左边的字符串和右边的字符串相同的时候就继续，然后，将右边的游标继续向右+1，左边的游标向左-1，如果左右的字符串相等，又继续这样干下去。。。
  > ```
  > class Solution:
  >     def longestPalindrome(self, s):
  >         """
  >         :type s: str
  >         :rtype: str
  >         """
  >         len_s = len(s)
  >         if len_s <= 1:
  >             return s
  >         max_left, max_right, max_len = 0, 0, 0
  >         for i in range(1, len_s):
  >             left = i - 1
  >             right = i + 1
  >             while (left >= 0 and right < len_s and left < right):
  >                 if s[left] == s[right]:
  >                     left -= 1
  >                     right += 1
  >                 else:
  >                     break
  >             tmp = right - left - 1
  >             if tmp > max_len:
  >                 max_len = tmp
  >                 max_left = left + 1
  >                 max_right = right - 1
  > 
  >         for i in range(1, len_s):
  >             left = i
  >             right = i + 1
  >             while (left >= 0 and right < len_s and left < right):
  >                 if s[left] == s[right]:
  >                     left -= 1
  >                     right += 1
  >                 else:
  >                     break
  >             tmp = right - left - 1
  >             if tmp > max_len:
  >                 max_len = tmp
  >                 max_left = left + 1
  >                 max_right = right - 1        
  >         return s[max_left, max_right + 1]
  > ```

+ 方法2：较为暴力的解法（来源于LeetCode所用时间最短的代码）

  > ```
  > class Solution:
  >     def longestPalindrome(self, s):
  >         """
  >         :type s: str
  >         :rtype: str
  >         """
  >         n = len(s)
  >         if n < 2 or s == s[::-1]:
  >             return s
  >         max_len = 1
  >         start = 0
  >         for i in range(1, n):
  >             even = s[i - max_len:i + 1]
  >             odd = s[i - max_len -1:i + 1]
  >             if i - max_len - 1 >= 0 and odd == odd[::-1]:
  >                 start = i - max_len - 1
  >                 # aba 
  >                 max_len += 2
  >                 continue
  >             if i - max_len >= 0 and even == even[::-1]:
  >                 start = i - max_len
  >                 # aa
  >                 max_len += 1
  >         return s[start:start + max_len]
  > ```

+ 方法3：Manacher's ALGORITHM
+ 不多说，附上大神解释的[链接](https://www.felix021.com/blog/read.php?2040)