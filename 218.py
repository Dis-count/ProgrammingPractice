# 面试题 17.09. Get Kth Magic Number LCCI
# Design an algorithm to find the kth number such that the only prime factors are 3, 5, and 7. Note that 3, 5, and 7 do not have to be factors, but it should not have any other prime factors. For example, the first several multiples would be (in order) 1, 3, 5, 7, 9, 15, 21.

# Example 1:

# Input: k = 5

# Output: 9

# 最小堆
import heapq

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        factors = [3, 5, 7]
        seen = {1}
        heap = [1]

        for i in range(k - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)

# 动态规划  三指针

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0] * (k + 1)
        dp[1] = 1
        p3 = p5 = p7 = 1

        for i in range(2, k + 1):
            num3, num5, num7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
            dp[i] = min(num3, num5, num7)
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
            if dp[i] == num7:
                p7 += 1
        
        return dp[k]

# 时间复杂度：O(k)。需要计算数组 dp 中的 k 个元素，每个元素的计算都可以在 O(1) 的时间内完成。
# 空间复杂度：O(k)。空间复杂度主要取决于数组 dp 的大小。

