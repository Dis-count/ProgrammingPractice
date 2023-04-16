# 2404. Most Frequent Even Element
# 提示
# 简单

# Given an integer array nums, return the most frequent even element.

# If there is a tie, return the smallest one. If there is no such element, return -1. 

# Example 1:

# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.

# Example 2:

# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.

# Example 3:

# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.

from typing import List
from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter()
        for x in nums:
            if x % 2 == 0:
                count[x] += 1
        res, ct = -1, 0
        for k, v in count.items():
            if res == -1 or v > ct or (v == ct and res > k):
                res = k
                ct = v
        return res


nums = [29,47,21,41,13,37,25,7]

res = Solution()
res.mostFrequentEven(nums)


