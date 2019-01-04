# 4. median-of-two-sorted-arrays

+ [题目链接](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

+ 1. 暴力解法：
>```
>class Solution:
>    def findMedianSortedArrays(self, nums1, nums2):
>        nums = nums1+nums2
>        nums.sort()
>        ret,more  = divmod(len(nums),2)
>        if more ==1:
>            return nums[ret]
>        else:
>            return (nums[ret]+nums[ret-1])/2
>```


+ 2. 官方思路
>+ 我们只需要处理三种情况：
>+ 1. (j = 0 or i = m or B[j-1] <= A[i]) 或者 (i = 0 or j = n or A[i-1] <= B[j])
>+ 2. i < m and B[j-1] > A[i]
>+ 3. i > 0 and A[i-1] > b[j]
>     ```
>     class Solution:
>         def findMedianSortedArrays(self, nums1, nums2):
>             len_1 = len(nums1)
>             len_2 = len(nums2)
>             if len_1 > len_2:
>                 return self.findMedianSortedArrays(nums2, nums1)
>             i_min = 0
>             i_max = len_1
>             while i_min <= i_max:
>                 i = (i_min + i_max) // 2
>                 j = (len_1 + len_2 + 1) // 2 - i
>                 if i < len_1 and nums1[i] < nums2[j-1]:
>                     i_min = i + 1
>                 elif i > 0 and nums1[i-1] > nums2[j]:
>                     i_max = i - 1
>                 else:
>                     if i == 0:
>                         max_left = nums2[j-1]
>                     elif j == 0:
>                         max_left = nums1[i-1]
>                     else:
>                         max_left = max(nums1[i-1], nums2[j-1])
>                     if (len_1 + len_2) % 2 == 1:
>                         return max_left
>                     if i == len_1:
>                         min_right = nums2[j]
>                     elif j == len_2:
>                         min_right = nums1[i]
>                     else:
>                         min_right = min(nums1[i], nums2[j])
>                     return (max_left + min_right) / 2
>     ```
>

+ 3. [看不懂的牛人解析法](http://chaoren.is-programmer.com/posts/42890.html)

  > + 首先转成求A和B数组中第k小的数的问题, 然后用k/2在A和B中分别找。比如k = 6, 分别看A和B中的第3个数, 已知 A1 < A2 < A3 < A4 < A5... 和 B1 < B2 < B3 < B4 < B5..., 如果A3 <＝ B3, 那么第6小的数肯定不会是A1, A2, A3, 因为最多有两个数小于A1, 三个数小于A2, 四个数小于A3。B3至少大于5个数, 所以第6小的数有可能是B1 (A1 < A2 < A3 < A4 < A5 < B1), 有可能是B2 (A1 < A2 < A3 < B1 < A4 < B2), 有可能是B3 (A1 < A2 < A3 < B1 < B2 < B3)。那就可以排除掉A1, A2, A3, 转成求A4, A5, ... B1, B2, B3, ...这些数中第3小的数的问题, k就被减半了。每次都假设A的元素个数少, pa = min(k/2, lenA)的结果可能导致k == 1或A空, 这两种情况都是终止条件。 
  >
  > ```
  > class Solution:
  >     def getMedian(self, A, B, k):
  >         # return kth smallest number of arrays A and B, assume len(A) <= len(B)
  >         lenA = len(A)
  >         lenB = len(B)
  >         if lenA > lenB: return self.getMedian(B, A, k)
  >         if lenA == 0: return B[k - 1]
  >         if k == 1: return min(A[0], B[0])
  >         pa = min(k / 2, lenA)
  >         pb = k - pa
  >         return self.getMedian(A[pa:], B, k - pa) if A[pa - 1] <= B[pb - 1] else self.getMedian(A, B[pb:], k - pb)
  > 
  >     def findMedianSortedArrays(self, A, B):
  >         lenA = len(A)
  >         lenB = len(B)
  >         if (lenA + lenB) % 2 == 1:
  >             return self.getMedian(A, B, (lenA + lenB) / 2 + 1)
  >         else:
  >             return 0.5 * (self.getMedian(A, B, (lenA + lenB) / 2) + self.getMedian(A, B, (lenA + lenB) / 2 + 1))
  > ```
