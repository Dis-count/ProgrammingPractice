# 673. Number of Longest Increasing Subsequence
# Given an integer array nums, return the number of longest increasing subsequences.
#
# Notice that the sequence has to be strictly increasing.
#
# Example 1:
#
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
#
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

# See Num 300.
# 定义 dp[i] 表示以 nums[i] 结尾的最长上升子序列的长度，cnt[i] 表示以 nums[i] 结尾的最长上升子序列的个数。
# 设 nums 的最长上升子序列的长度为 maxLen，那么答案为所有满足 dp[i]=maxLen 的 i 所对应的 cnt[i] 之和。
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n, max_len, ans = len(nums), 0, 0
        dp = [0] * n
        cnt = [0] * n
        for i, x in enumerate(nums):
            dp[i] = 1
            cnt[i] = 1
            for j in range(i):
                if x > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]  # 重置计数
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > max_len:
                max_len = dp[i]
                ans = cnt[i]  # 重置计数
            elif dp[i] == max_len:
                ans += cnt[i]
        return ans

# 时间复杂度：O(n^2)，其中 n 是数组 nums 的长度。
# 空间复杂度：O(n)。

# 方法二：贪心 + 前缀和 + 二分查找
from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        d, cnt = [], []
        for v in nums:
            i = bisect(len(d), lambda i: d[i][-1] >= v)
            c = 1
            if i > 0:
                k = bisect(len(d[i - 1]), lambda k: d[i - 1][k] < v)
                c = cnt[i - 1][-1] - cnt[i - 1][k]
            if i == len(d):
                d.append([v])
                cnt.append([0, c])
            else:
                d[i].append(v)
                cnt[i].append(cnt[i][-1] + c)
        return cnt[-1][-1]

    def bisect(n: int, f: Callable[[int], bool]) -> int:
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if f(mid):
                r = mid
            else:
                l = mid + 1
        return l
