# 面试题 01.08. Zero Matrix LCCI
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

# Example 1:

# Input:
# [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]
# Output:
# [
#     [1, 0, 1],
#     [0, 0, 0],
#     [1, 0, 1]
# ]

# Example 2:

# Input:
# [
#     [0, 1, 2, 0],
#     [3, 4, 5, 2],
#     [1, 3, 1, 5]
# ]
# Output:
# [
#     [0, 0, 0, 0],
#     [0, 4, 5, 0],
#     [0, 3, 1, 0]
# ]

#  直接模拟
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0

# 使用一个变量标记

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0

# 主要是优化空间复杂度

matrix = [[0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]]

s = Solution()
s.setZeroes(matrix)
print(matrix)