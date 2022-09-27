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