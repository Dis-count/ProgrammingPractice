# 1799. Maximize Score After N Operations
# 困难

# You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

# In the ith operation (1-indexed), you will:

# Choose two elements, x and y.
# Receive a score of i * gcd(x, y).
# Remove x and y from nums.
# Return the maximum score you can receive after performing n operations.

# The function gcd(x, y) is the greatest common divisor of x and y.


# Example 1:

# Input: nums = [1,2]
# Output: 1
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 2)) = 1

# Example 2:

# Input: nums = [3,4,6,8]
# Output: 11
# Explanation: The optimal choice of operations is:
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

# Example 3:

# Input: nums = [1,2,3,4,5,6]
# Output: 14
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14

# 用二进制表示是否使用 第 i 位
#  ^ 用于删去 i,j : 亦或相同为0
#  & 用于判断存在: 同为1 则为1 

from typing import List
from math import gcd

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)
        g = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                g[i][j] = gcd(nums[i], nums[j])
        f = [0] * (1 << m)
        for k in range(1 << m):
            if (cnt := k.bit_count()) % 2 == 0:
                for i in range(m):
                    if k >> i & 1:  # 存在第 i 
                        for j in range(i + 1, m):
                            if k >> j & 1:  #  存在j 
                                f[k] = max(f[k], f[k ^ (1 << i) ^ (1 << j)] + cnt // 2 * g[i][j])
        print(f)
        return f[-1]

nums = [6,3,4,5]

test = Solution()
test.maxScore(nums)
