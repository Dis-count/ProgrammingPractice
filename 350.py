# 1031. Maximum Sum of Two Non-Overlapping Subarrays
# 提示
# 中等

# Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

# The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

# Example 2:
# Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

# Example 3:
# Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.

from typing import List
from itertools import accumulate

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = list(accumulate(nums, initial=0))  # nums 的前缀和
        ans = 0
        def f(firstLen: int, secondLen: int) -> None:
            nonlocal ans
            maxSumA = 0
            for i in range(firstLen + secondLen, len(s)):
                maxSumA = max(maxSumA, s[i - secondLen] - s[i - secondLen - firstLen])
                ans = max(ans, maxSumA + s[i] - s[i - secondLen])
        f(firstLen, secondLen)  # 左 a 右 b
        f(secondLen, firstLen)  # 左 b 右 a
        return ans

nums = [0,6,5,2,2,5,1,9,4]

list(accumulate(nums, initial=0))

#  简化

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = list(accumulate(nums, initial=0))  # nums 的前缀和
        ans = maxSumA = maxSumB = 0
        for i in range(firstLen + secondLen, len(s)):
            maxSumA = max(maxSumA, s[i - secondLen] - s[i - firstLen - secondLen])
            maxSumB = max(maxSumB, s[i - firstLen] - s[i - firstLen - secondLen])
            ans = max(ans, maxSumA + s[i] - s[i - secondLen], maxSumB + s[i] - s[i - firstLen])
        return ans
