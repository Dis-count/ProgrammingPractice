# 1658. Minimum Operations to Reduce X to Zero
# 中等

# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

# Example 1:
# Input: nums = [1, 1, 4, 2, 3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

# Example 2:
# Input: nums = [5, 6, 7, 8, 9], x = 4
# Output: -1

# Example 3:
# Input: nums = [3, 2, 20, 1, 1, 3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements(5 operations in total) to reduce x to zero.

# 滑动窗口
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)

        if total < x:
            return -1
        
        right = 0
        lsum, rsum = 0, total
        ans = n + 1
        for left in range(-1, n - 1):
            if left != -1:
                lsum += nums[left]
            while right < n and lsum + rsum > x:
                rsum -= nums[right]
                right += 1
            if lsum + rsum == x:
                ans = min(ans, (left + 1) + (n - right))
        
        return -1 if ans > n else ans

# 时间复杂度：O(n)，其中 n 是数组 nums 的长度。left 和 right 均最多遍历整个数组一次。
# 空间复杂度：O(1)。