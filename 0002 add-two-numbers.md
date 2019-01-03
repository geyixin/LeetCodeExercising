# 两数相加（add-two-numbers）

+ [原题链接](https://leetcode-cn.com/problems/add-two-numbers/)

+ 递归实现：

  ```
  class Solution(object):
      def addTwoNumbers(self, l1, l2):
          if not l1 and not l2:
              return
          elif not (l1 and l2):
              return l1 or l2
          tmp = l1.val + l2.val
          if tmp < 10:
              l3 = ListNode(tmp)
              l3.next = self.addTwoNumbers(l1.next, l2.next)
          else:
              l3 = ListNode(tmp - 10)
              l3.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
          return l3
  ```

+ 非递归实现：

  ```
  class Solution(object):
      def addTwoNumbers(self, l1, l2):
          rem = 0
          dummy = ListNode(0)
          p = dummy
          while l1 or l2 or rem:
              s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + rem
              rem = s/10
              p.next = ListNode(s%10)
              p = p.next
              if l1:
                  l1 = l1.next
              if l2:
                  l2 = l2.next
          return dummy.next
  ```