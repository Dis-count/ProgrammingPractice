# 1877. Minimize Maximum Pair Sum in Array
# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
#
# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
#
# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.
#
# Example 1:
#
# Input: nums = [3,5,2,3]
# Output: 7
# Explanation: The elements can be paired up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
#
# Example 2:
#
# Input: nums = [3,5,4,2,4,6]
# Output: 8
# Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
# The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.

#  排序+贪心

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        for i in range(n // 2):
            res = max(res, nums[i] + nums[n-1-i])
        return res

# 复杂度分析
# 时间复杂度：O(nlogn)，其中 n 为数组 nums 的长度。排序 nums 的时间复杂度为 O(nlogn)，遍历维护最大数对和的时间复杂度为O(n)。
# 空间复杂度：O(logn)，即为排序的栈空间开销。
