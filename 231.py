# 801. Minimum Swaps To Make Sequences Increasing
# You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].

# For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
# Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.

# An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].


# Example 1:

# Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
# Output: 1
# Explanation: 
# Swap nums1[3] and nums2[3]. Then the sequences are:
# nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
# which are both strictly increasing.

# Example 2:

# Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
# Output: 1

# 动态规划
# 可以设 dp[i][0] 表示到位置 i 为止使数组 nums1 和 nums2
# 满足严格递增并且位置 i 不进行交换操作的最小操作数，设 dp[i][1] 表示到位置 i 为止使数组 
# nums1​ 和 nums2 满足严格递增并且位置 i 进行交换操作的最小操作数


from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a, b = 0, 1
        for i in range(1, n):
            at, bt = a, b
            a = b = n
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                a = min(a, at)
                b = min(b, bt + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                a = min(a, bt)
                b = min(b, at + 1)
        return min(a, b)

# 时间复杂度：O(n)，其中 n 为数组 nums1 和 nums2 的长度。需要遍历两个数组一次，每个状态的计算时间是 O(1)。
# 空间复杂度：O(1)O(1)。使用「滚动数组」后，仅使用常量空间。
