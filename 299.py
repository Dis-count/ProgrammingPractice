# 1814. Count Nice Pairs in an Array
# 中等

# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices(i, j) is nice if it satisfies all of the following conditions:

# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 10^9 + 7.

# Example 1:

# Input: nums = [42, 11, 1, 97]
# Output: 2
# Explanation: The two pairs are:
#  - (0, 3): 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1, 2): 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

# Example 2:

# Input: nums = [13, 10, 35, 24, 76]
# Output: 4

from typing import List
from collections import Counter

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res = 0
        cnt = Counter()
        for i in nums:
            j = int(str(i)[::-1])
            res += cnt[i - j]
            cnt[i - j] += 1
            print(cnt)
        return res % (10 ** 9 + 7)


nums = [13, 10, 35, 24, 76]

test =Solution()
test.countNicePairs(nums)

# \geometry{a4paper,left=1in,right=1in,top =1in, bottom = 1in}