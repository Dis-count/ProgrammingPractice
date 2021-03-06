# 363. Max Sum of Rectangle No Larger Than K
# Given an (m x n matrix) matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.
#
# It is guaranteed that there will be a rectangle with a sum no larger than k.
#
# Example 1:
#
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
#
# Example 2:
#
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3

# 转化为「在一维数组中，求解和不超过 K 的最大连续子数组之和」


# 1. 划分左右边界，并求出在此边界下，每行的总和
# 2. 通过二分法找不超过K的矩阵

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        for left in range(col):
            # 以left为左边界，每行的总和
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                # 在left，right为边界下的矩阵，求不超过K的最大数值和
                arr = [0]
                cur = 0
                for tmp in _sum:
                    cur += tmp
                    # 二分法
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):res = max(cur - arr[loc], res)
                    # 把累加和加入
                    bisect.insort(arr, cur)
        return res
