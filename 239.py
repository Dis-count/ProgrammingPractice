# 891. Sum of Subsequence Widths
# 困难

# The width of a sequence is the difference between the maximum and minimum elements in the sequence.

# Given an array of integers nums, return the sum of the widths of all the non-empty subsequences of nums. Since the answer may be very large, return it modulo 10e9 + 7.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3, 6, 2, 7] is a subsequence of the array[0, 3, 1, 6, 2, 2, 7].


# Example 1:

# Input: nums = [2, 1, 3]
# Output: 6
# Explanation: The subsequences are[1], [2], [3], [2, 1], [2, 3], [1, 3], [2, 1, 3].
# The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
# The sum of these widths is 6.
# Example 2:

# Input: nums = [2]
# Output: 0
from typing import List

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        MOD = 10 ** 9 + 7
        x, y = nums[0], 2
        for j in range(1, len(nums)):
            res = (res + nums[j] * (y - 1) - x) % MOD
            x = (x * 2 + nums[j]) % MOD
            y = y * 2 % MOD
        return (res + MOD) % MOD


# 复杂度分析

# 时间复杂度：O(nlog⁡n)，其中 n 是数组 nums 的长度。排序需要 O(nlog⁡n)，求解所有 Bj​  需要 O(n)。

# 空间复杂度：O(log⁡n)。排序需要 O(log⁡n) 的栈空间。
