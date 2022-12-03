"""
@Author      :   Discount 
@Time        :   03/12/2022 14:27:11
@Description :   
"""

# 1796. Second Largest Digit in a String
# 简单

# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

# An alphanumeric string is a string consisting of lowercase English letters and digits.


# Example 1:

# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.


# Example 2:

# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit. 

class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1
        for c in s:
            if c.isdigit():
                num = int(c)
                if num > first:
                    second = first
                    first = num
                elif second < num < first:
                    second = num
        return second

# 时间复杂度：O(n)，其中 n 表示字符串的长度。我们只需遍历一遍字符串即可。
# 空间复杂度：O(1)。仅需常数个空间即可。
