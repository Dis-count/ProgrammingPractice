# 1027. Longest Arithmetic Subsequence
# 中等

# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

# Note that:

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
 
# Example 1:

# Input: nums = [3,6,9,12]
# Output: 4
# Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
# Example 2:

# Input: nums = [9,4,7,2,10]
# Output: 3
# Explanation:  The longest arithmetic subsequence is [4,7,10].
# Example 3:

# Input: nums = [20,1,15,3,10,5,8]
# Output: 4
# Explanation:  The longest arithmetic subsequence is [20,15,10,5].

from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        minv, maxv = min(nums), max(nums)
        diff = maxv - minv
        ans = 1

        for d in range(-diff, diff + 1):
            f = dict()
            for num in nums:
                if (prev := num - d) in f:
                    f[num] = max(f.get(num, 0), f[prev] + 1)
                    ans = max(ans, f[num])
                f[num] = max(f.get(num, 0), 1)
        
        return ans

nums = [9,4,7,2,10]

test = Solution()
test.longestArithSeqLength(nums)
