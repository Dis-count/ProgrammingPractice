# 面试题 01.09. String Rotation LCCI
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1(e.g., "waterbottle" is a rotation of"erbottlewat"). Can you use only one call to the method that checks if one word is a substring of another?

# Example 1:

# Input: s1 = "waterbottle", s2 = "erbottlewat"
# Output: True

# Example 2:

# Input: s1 = "aa", s2 = "aba"
# Output: False

#  搜索子字符串

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in s1 + s1

