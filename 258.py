# 1775. Equal Sum Arrays With Minimum Number of Operations
# 中等

# You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

# In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

# Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

# Example 1:

# Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
# Output: 3
# Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
# - Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
# - Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
# - Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].

# Example 2:

# Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
# Output: -1
# Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.

# Example 3:

# Input: nums1 = [6,6], nums2 = [1]
# Output: 3
# Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
# - Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
# - Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
# - Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].

#  贪心 help + 哈希表 cnt1
from typing import List

class Solution:
    def help(self, h1: List[int], h2: List[int], diff: int) -> int:
        h = [0] * 7
        for i in range(1, 7):
            h[6 - i] += h1[i]
            h[i - 1] += h2[i]
        res = 0
        for i in range(5, 0, -1):
            if diff <= 0: break
            t = min((diff + i - 1) // i, h[i])
            res += t
            diff -= t * i
        return res

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        if 6 * n < m or 6 * m < n:
            return -1
        cnt1 = [0] * 7
        cnt2 = [0] * 7
        diff = 0
        for i in nums1:
            cnt1[i] += 1
            diff += i
        for i in nums2:
            cnt2[i] += 1
            diff -= i
        if diff == 0:
            return 0
        if diff > 0:
            return self.help(cnt2, cnt1, diff)
        return self.help(cnt1, cnt2, -diff)

# 时间复杂度：O(n+m)，其中 n，m 分别为数组 nums1 ​ nums2 的长度。
# 空间复杂度：O(C)，其中 C 为数组 nums1，nums2 中元素值的取值空间，主要为用数组来模拟「哈希表」的空间开销。
