# 795. Number of Subarrays with Bounded Maximum
# 中等

# Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:

# Input: nums = [2,1,4,3], left = 2, right = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

# Example 2:

# Input: nums = [2,9,2,5,6], left = 2, right = 8
# Output: 7

# nums will be divided into several parts according to the position of the number which is larger than right

#  单次遍历

from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        last2 = last1 = -1
        for i, x in enumerate(nums):
            if left <= x <= right:
                last1 = i
            elif x > right:
                last2 = i
                last1 = -1
            if last1 != -1:
                res += last1 - last2
            print(f'process:{res}')
        return res

nums = [2,9,2,5,6] 
left = 2
right = 8

test = Solution()
test.numSubarrayBoundedMax(nums, left, right)


#  计数

#  the number of subarray containing 0,1 - the number of containing only 0.

class Solution1:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(lower: int) -> int:
            res = cur = 0
            for x in nums:
                if x <= lower:
                    cur += 1
                else:
                    cur = 0
                res += cur
            return res
        return count(right) - count(left - 1)

# notice it is left-1.