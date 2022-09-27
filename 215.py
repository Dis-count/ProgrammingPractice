# 788. Rotated Digits
# An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. For example:

# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become invalid.
# Given an integer n, return the number of good integers in the range [1, n].


# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

# Example 2:

# Input: n = 1
# Output: 0

# Example 3:

# Input: n = 2
# Output: 1
 

# Constraints:
# 1 <= n <= 10^4

class Solution:
    def rotatedDigits(self, n: int) -> int:
        check = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]

        ans = 0
        for i in range(1, n + 1):
            num = [int(digit) for digit in str(i)]
            valid, diff = True, False
            for digit in num:
                if check[digit] == -1:
                    valid = False
                elif check[digit] == 1:
                    diff = True
            if valid and diff:
                ans += 1
        
        return ans

# 1. 直接模拟

# 2. 数位dp
from functools import cache

DIFFS = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)

        @cache
        def f(i: int, has_diff: bool, is_limit: bool) -> int:
            if i == len(s):
                return has_diff  # 只有包含 2/5/6/9 才算一个好数
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(0, up + 1):  # 枚举要填入的数字 d
                if DIFFS[d] != -1:  # d 不是 3/4/7
                    res += f(i + 1, has_diff or DIFFS[d], is_limit and d == up)
            return res
        return f(0, False, True)

