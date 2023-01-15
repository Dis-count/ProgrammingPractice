# 1819. Number of Different Subsequences GCDs
# 困难

# You are given an array nums that consists of positive integers.

# The GCD of a sequence of numbers is defined as the greatest integer that divides all the numbers in the sequence evenly.

# For example, the GCD of the sequence[4, 6, 16] is 2.
# A subsequence of an array is a sequence that can be formed by removing some elements(possibly none) of the array.

# For example, [2, 5, 10] is a subsequence of[1, 2, 1, 2, 4, 1, 5, 10].
# Return the number of different GCDs among all non-empty subsequences of nums.


# Example 1:
# Input: nums = [6, 10, 3]
# Output: 5
# Explanation: The figure shows all the non-empty subsequences and their GCDs.
# The different GCDs are 6, 10, 3, 2, and 1.

# Example 2:

# Input: nums = [5, 15, 40, 5, 6]
# Output: 7

#  反向枚举  枚举每一个从 1- max_num 的数

from typing import List
from math import gcd


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        ans, mx = 0, max(nums)
        has = [False] * (mx + 1)
        for x in nums:
            has[x] = True
        for i in range(1, mx + 1):
            g = 0  # 0 和任何数 x 的最大公约数都是 x
            for j in range(i, mx + 1, i):  # 枚举 i 的倍数 j
                if has[j]:  # 如果 j 在 nums 中
                    g = gcd(g, j)  # 更新最大公约数
                    if g == i:  # 找到一个答案（g 无法继续减小）
                        ans += 1
                        break  # 提前退出循环
        return ans


#  两层循环： 1: i 从1-max_num; 2: for each i's 倍数 
#  注意第二层循环不是 在原数组 中找 i 的倍数，而是在max 范围内找 i 的倍数