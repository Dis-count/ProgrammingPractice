# 931. Minimum Falling Path Sum
# 中等

# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


# Example 1:

# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:

# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.

from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0]
        for i in range(1, n):
            cur = [0] * n
            for j in range(n):
                mn = dp[j]
                if j > 0:
                    mn = min(mn, dp[j - 1])
                if j < n - 1:
                    mn = min(mn, dp[j + 1])
                cur[j] = mn + matrix[i][j]
            dp = cur
        return min(dp)
    
matrix = [[-84,-36,2],[87,-79,10],[42,10,63]]

test = Solution()
res = test.minFallingPathSum(matrix)

print(res)

from math import inf

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        f = [inf] + matrix[0] + [inf]
        for row in matrix[1:]:
            pre = f[0]  # 充当 f[c]
            for c, x in enumerate(row):
                pre, f[c + 1] = f[c + 1], min(pre, f[c + 1], f[c + 2]) + x
        return min(f)
