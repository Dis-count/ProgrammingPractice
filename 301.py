"""
@Author      :   Discount 
@Time        :   27/01/2023 13:09:25
@Description :   
"""

# 2309. Greatest English Letter in Upper and Lower Case
# 简单

# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

# An English letter b is greater than another letter a if b appears after a in the English alphabet.


# Example 1:

# Input: s = "lEeTcOdE"
# Output: "E"
# Explanation:
# The letter 'E' is the only letter to appear in both lower and upper case.
# Example 2:

# Input: s = "arRAzFif"
# Output: "R"
# Explanation:
# The letter 'R' is the greatest letter to appear in both lower and upper case.
# Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.
# Example 3:

# Input: s = "AbCdEfGhIjK"
# Output: ""
# Explanation:
# There is no letter that appears in both lower and upper case.

#  一次 & 存在 用哈希

from string import ascii_lowercase
from string import ascii_uppercase

class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for lower, upper in zip(reversed(ascii_lowercase), reversed(ascii_uppercase)):
            if lower in s and upper in s:
                return upper
        return ""

# reversed ---> greatest

s = "arRAzFif"

set(s)
