# 1937. Maximum Number of Points with Cost
# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
#
# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
#
# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
#
# Return the maximum number of points you can achieve.
#
# abs(x) is defined as:
#
# x for x >= 0.
# -x for x < 0.
#
# Example 1:
#
#
# Input: points = [[1,2,3],[1,5,1],[3,1,1]]
# Output: 9
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
# You add 3 + 5 + 3 = 11 to your score.
# However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
# Your final score is 11 - 2 = 9.
# Example 2:
#
#
# Input: points = [[1,5],[2,3],[4,2]]
# Output: 11
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
# You add 5 + 3 + 4 = 12 to your score.
# However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
# Your final score is 12 - 1 = 11.

#  动态规划
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        f = [0] * n
        for i in range(m):
            g = [0] * n
            best = float("-inf")
            # 正序遍历
            for j in range(n):
                best = max(best, f[j] + j)
                g[j] = max(g[j], best + points[i][j] - j)

            best = float("-inf")
            # 倒序遍历
            for j in range(n - 1, -1, -1):
                best = max(best, f[j] - j)
                g[j] = max(g[j], best + points[i][j] + j)

            f = g

        return max(f)

points = [[1,5],[2,3],[4,2]]
a = Solution()
a.maxPoints(points)

# 复杂度分析
# 时间复杂度：O(mn)。
# 空间复杂度：O(n)。
