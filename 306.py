# 1798. Maximum Number of Consecutive Values You Can Make
# 中等

# You are given an integer array coins of length n which represents the n coins that you own. The value of the ith coin is coins[i]. You can make some value x if you can choose some of your n coins such that their values sum up to x.

# Return the maximum number of consecutive integer values that you can make with your coins starting from and including 0.

# Note that you may have multiple coins of the same value.


# Example 1:

# Input: coins = [1, 3]
# Output: 2
# Explanation: You can make the following values:
# - 0: take[]
# - 1: take[1]
# You can make 2 consecutive integer values starting from 0.
# Example 2:

# Input: coins = [1, 1, 1, 4]
# Output: 8
# Explanation: You can make the following values:
# - 0: take[]
# - 1: take[1]
# - 2: take[1, 1]
# - 3: take[1, 1, 1]
# - 4: take[4]
# - 5: take[4, 1]
# - 6: take[4, 1, 1]
# - 7: take[4, 1, 1, 1]
# You can make 8 consecutive integer values starting from 0.
# Example 3:

# Input: nums = [1, 4, 10, 3, 1]
# Output: 20

#  贪心

from typing import List

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        m = 0  # 一开始只能构造出 0
        coins.sort()
        for c in coins:
            if c > m + 1:  # coins 已排序，后面没有比 c 更小的数了
                break  # 无法构造出 m+1，继续循环没有意义
            m += c  # 可以构造出区间 [0,m+c] 中的所有整数
        return m + 1  # [0,m] 中一共有 m+1 个整数
