#!/usr/bin/env python
# -*- coding:utf-8 -*-


##################------------###################
"""
第一个是我自己所想，用的递归。
第二个是提交成功显示的时间最短的。
"""
##################------------###################



"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        sum = 0
        for employee in employees:
            if employee.id == id:
                sum += employee.importance
                # print(sum)
                for i in employee.subordinates:
                    sum += self.getImportance(employees, i)
        return sum



# class Solution:
#     def getImportance(self, employees, id):
#         """
#         :type employees: Employee
#         :type id: int
#         :rtype: int
#         """
#         total = 0
#         id_dic = {}
#         for emp in employees:
#             id_dic[emp.id] = (emp.importance, emp.subordinates)
#         subordinate = id_dic[id][1]
#         total += id_dic[id][0]
#         for s in subordinate:
#             total += id_dic[s][0]
#             subordinate += id_dic[s][1]
#         return total