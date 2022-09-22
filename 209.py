# 1636. Sort Array by Increasing Frequency
# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

# Example 1:

# Input: nums = [1, 1, 2, 2, 2, 3]
# Output: [3, 1, 1, 2, 2, 2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

# Example 2:

# Input: nums = [2, 3, 1, 3, 2]
# Output: [1, 3, 3, 2, 2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

# Example 3:

# Input: nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
# Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]

#  模拟

# 按着题目的要求，先算出数组 nums 中各元素的频率，然后按照元素频率和数值对数组进行排序即可。
from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        nums.sort(key = lambda x: (cnt[x], -x))
        return nums

#  先按元素个数升序 再按大小降序排列
# 复杂度分析

# 时间复杂度：O(nlogn)，其中 n 是数组 nums 的长度。排序消耗 O(nlogn) 时间。

# 空间复杂度：O(n)，存储数组元素频率的哈希表消耗 O(n) 空间。

nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
s = Solution()
s.frequencySort(nums)
