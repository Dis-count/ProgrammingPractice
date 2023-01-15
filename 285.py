# 1802. Maximum Value at a Given Index in a Bounded Array
# 中等

# You are given three positive integers: n, index, and maxSum. You want to construct an array nums(0-indexed) that satisfies the following conditions:

# nums.length == n
# nums[i] is a positive integer where 0 <= i < n.
# abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# The sum of all the elements of nums does not exceed maxSum.
# nums[index] is maximized.
# Return nums[index] of the constructed array.

# Note that abs(x) equals x if x >= 0, and -x otherwise.

# Example 1:
# Input: n = 4, index = 2,  maxSum = 6
# Output: 2
# Explanation: nums = [1, 2, 2, 1] is one array that satisfies all the conditions.
# There are no arrays that satisfy all the conditions and have nums[2] == 2, so 2 is the maximum nums[2].

# Example 2:
# Input: n = 6, index = 1,  maxSum = 10
# Output: 3

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.valid(mid, n, index, maxSum):
                left = mid
            else:
                right = mid - 1
        return left

    def valid(self, mid: int, n: int, index: int, maxSum: int) -> bool:
        left = index
        right = n - index - 1
        return mid + self.cal(mid, left) + self.cal(mid, right) <= maxSum

    def cal(self, big: int, length: int) -> int:
        if length + 1 < big:
            small = big - length
            return ((big - 1 + small) * length) // 2
        else:
            ones = length - (big - 1)
            return (big - 1 + 1) * (big - 1) // 2 + ones