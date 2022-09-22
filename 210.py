# 698. Partition to K Equal Sum Subsets
# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

# Example 1:

# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets(5), (1, 4), (2, 3), (2, 3) with equal sums.

# Example 2:

# Input: nums = [1, 2, 3, 4], k = 3
# Output: false

# Constraints:

# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 104
# The frequency of each element is in the range[1, 4].
from typing import List
from functools import cache


# 1. 状态压缩 + 记忆化搜索
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        all = sum(nums)
        if all % k:
            return False
        per = all // k
        nums.sort()  # 方便下面剪枝
        if nums[-1] > per:
            return False
        n = len(nums)

        @cache
        def dfs(s, p):
            if s == 0:
                return True
            for i in range(n):
                if nums[i] + p > per:
                    break
                if s >> i & 1 and dfs(s ^ (1 << i), (p + nums[i]) % per):  # p + nums[i] 等于 per 时置为 0
                    return True
            return False
        return dfs((1 << n) - 1, 0)

# 其中 s 需要以二进制来观察，每一位代表每个数字的使用状态
#  p 代表当前这个桶已经积累了多少值

#  判断第i个数是否为使用过
#  s >> i 是将s左移i位，则此时的第一位就是s的第i位，再与（&）1，结果为1的话，则s的第i位为1，说明没被使用过
#  s由低位到高位分别对应第1到第n个数是否使用

#  s ^ (1 << i) 表示异或，相异为真，之前为0的，遇见除第i位以外的0还是为0，而之前为1的则还为1
#  只有s的第i位一定是1，遇到1会变成0，因此这个操作就是将s的第i位由1置为0，其他部分不变
#  后面之所以要取余，是因为本题不考虑相同数字的顺序，只有一种组合
#  那么只要依次找到这个组合里的几个子集即可，因此通过取余将p归0，相当于开始查找一个新子集

# time complexity: O(n 2^n)
# space complexity: O(2^n)

nums = [1, 2, 3, 4]

# 方法二：状态压缩 + 动态规划
# 思路与算法

# 我们同样可以用「动态规划」这种「自底向上」的方法来求解是否存在可行方案：同样我们用一个整数 S 来表示当前可用的数字集合：从低位到高位，第 i 位为 0 则表示数字 nums[i] 可以使用，否则表示 nums[i] 已被使用。然后我们用 dp[S] 来表示在可用的数字状态为 S 的情况下是否可能可行，初始全部状态为记录为不可行状态 False，只记 \textit{dp}[0] = \text{True}dp[0] = True 为可行状态。同样我们每次对于当前状态下从可用的数字中选择一个数字，若此时选择全部数字取模后小于等于 \textit{per}per。则说明选择该数字后的状态再继续往下添加数字是可能能满足题意的，并且此时标记状为可能可行状态，否则就一定不能达到满足。最终 dp[U] 即可，其中 U 表示全部数字使用的集合状态。


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        all = sum(nums)
        if all % k:
            return False
        per = all // k
        nums.sort()
        if nums[-1] > per:
            return False
        n = len(nums)
        dp = [False] * (1 << n)
        dp[0] = True
        cursum = [0] * (1 << n)
        for i in range(0, 1 << n):
            if not dp[i]:
                continue
            for j in range(n):
                if cursum[i] + nums[j] > per:
                    break
                if (i >> j & 1) == 0:
                    next = i | (1 << j)
                    if not dp[next]:
                        cursum[next] = (cursum[i] + nums[j]) % per
                        dp[next] = True
        return dp[(1 << n) - 1]
