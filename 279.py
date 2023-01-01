"""
@Author      :   Discount 
@Time        :   29/12/2022 12:26:27
@Description :   
"""

# 2032. Two Out of Three
# 简单

# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

# Example 1:

# Input: nums1 = [1, 1, 3, 2], nums2 = [2, 3], nums3 = [3]
# Output: [3, 2]
# Explanation: The values that are present in at least two arrays are:
# - 3, in all three arrays.
# - 2, in nums1 and nums2.

# Example 2:

# Input: nums1 = [3, 1], nums2 = [2, 3], nums3 = [1, 2]
# Output: [2, 3, 1]
# Explanation: The values that are present in at least two arrays are:
# - 2, in nums2 and nums3.
# - 3, in nums1 and nums2.
# - 1, in nums1 and nums3.

# Example 3:

# Input: nums1 = [1, 2, 2], nums2 = [4, 3, 3], nums3 = [5]
# Output: []
# Explanation: No value is present in at least two arrays.

from collections import defaultdict
from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        mask = defaultdict(int)
        for i, nums in enumerate((nums1, nums2, nums3)):
            for x in nums:
                mask[x] |= 1 << i
                print(mask)
        return [x for x, m in mask.items() if m & (m - 1)]

# 用 1 << i   表示数字出现在第几个 nums 里
# |= 1 << i   用于添加数字所在的组
# m & (m - 1) 用于判断是否有两个或以上的数字出现

nums1 = [1, 1, 3, 2] 
nums2 = [2, 3]
nums3 = [3]
test =Solution()

test.twoOutOfThree(nums1,nums2,nums3)
