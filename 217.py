# 面试题 01.02. Check Permutation LCCI
# Given two strings, write a method to decide if one is a permutation of the other.

# Example 1:

# Input: s1 = "abc", s2 = "bca"
# Output: true

# Example 2:

# Input: s1 = "abc", s2 = "bad"
# Output: false

# Note:

# 0 <= len(s1) <= 100
# 0 <= len(s2) <= 100

#  排序后进行比较

#  哈希表 记录每种字符的出现次数
# 根据题意，对两字符串进行词频统计，统计过程中使用变量 tot 记录词频不同的字符个数

from collections import Counter

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)


# 时间复杂度：O(n)
