class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        len_x = len(matrix)  # matrix.shape[0] But need import numpy!
        len_y = len(matrix[0])  # matrix.shape[1]
        zero_list_x = []
        zero_list_y = []
        for i in range(len_x):
            for j in range(len_y):
                if matrix[i][j] == 0:
                    zero_list_x.append(i)
                    zero_list_y.append(j)
        set_zero_x = set(zero_list_x)
        set_zero_y = set(zero_list_y)
        for i in range(len_x):
            for j in range(len_y):
                if matrix[i][j] != 0:
                    if i in set_zero_x:
                        matrix[i][j] = 0
                    if j in set_zero_y:
                        matrix[i][j] = 0

        # return matrix


# mm = [
#         [1, 1, 1],
#         [1, 0, 1],
#         [1, 1, 1]
#     ]
# mm = [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# ss = Solution()
# zz = ss.setZeroes(mm)
# print(zz)