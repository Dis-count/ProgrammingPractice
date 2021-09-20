# 1893. Check if All the Integers in a Range Are Covered
# You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.
#
# Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.
#
# An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.
#
#
# Example 1:
#
# Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
# Output: true
# Explanation: Every integer between 2 and 5 is covered:
# - 2 is covered by the first range.
# - 3 and 4 are covered by the second range.
# - 5 is covered by the third range.
#
# Example 2:
#
# Input: ranges = [[1,10],[10,20]], left = 21, right = 21
# Output: false
# Explanation: 21 is not covered by any range.

# 按题意 直接暴力

#  差分数组

from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52   # 差分数组
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1
        # 前缀和
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True

# 复杂度分析
#
# 时间复杂度：O(n+l)，其中 n 为 ranges 的长度，l 为 diff 的长度。初始化 diff 数组的时间复杂度为 O(l)，遍历 ranges 更新差分数组的时间复杂度为 O(n)，求解前缀和并判断是否完全覆盖的时间复杂度为 O(l)。
# 空间复杂度：O(l)，即为 diff 的长度。
