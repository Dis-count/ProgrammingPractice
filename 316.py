# 1124. Longest Well-Performing Interval
# 中等

# We are given hours, a list of the number of hours worked per day for a given employee.

# A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

# A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

# Return the length of the longest well-performing interval.

# Example 1:

# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].

# Example 2:

# Input: hours = [6,6,6]
# Output: 0

# 前缀和 + 单调栈
from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        # 大于8小时计1分 小于等于8小时计-1分
        score = [0] * n
        for i in range(n):
            if hours[i] > 8:
                score[i] = 1
            else:
                score[i] = -1
        
        # 前缀和
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + score[i - 1]
        ans = 0
        stack = []
        
        # 顺序生成单调栈，栈中元素从第一个元素开始严格单调递减，最后一个元素肯定是数组中的最小元素所在位置
        for i in range(n + 1):
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i)
        
        # 倒序扫描数组，求最大长度坡
        i = n
        while i > ans:
            while stack and presum[stack[-1]] < presum[i]:
                ans = max(ans, i - stack[-1])
                stack.pop()
            i -= 1
        return ans

class Solution0:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        s = [0] * (n + 1)  # 前缀和
        st = [0]  # s[0]
        for j, h in enumerate(hours, 1):
            s[j] = s[j - 1] + (1 if h > 8 else -1)
            if s[j] < s[st[-1]]: st.append(j)  # 感兴趣的 j
        ans = 0
        for i in range(n, 0, -1):
            while st and s[i] > s[st[-1]]:
                ans = max(ans, i - st.pop())  # [st[-1],i) 可能是最长子数组
        return ans

#  注意如果此题用滑动窗口则是双指针 复杂度：n^2
#  当 不能通过一些条件判断怎么移动这个窗口 时不能用滑动窗口