# 970. Powerful Integers
# 中等

# Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

# An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

# You may return the answer in any order. In your answer, each value should occur at most once.


# Example 1:

# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation:
# 2 = 20 + 30
# 3 = 21 + 30
# 4 = 20 + 31
# 5 = 21 + 31
# 7 = 22 + 31
# 9 = 23 + 30
# 10 = 20 + 32

# Example 2:

# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]

# 枚举

from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        value1 = 1
        for i in range(21):
            value2 = 1
            for j in range(21):
                value = value1 + value2
                if value <= bound:
                    res.add(value)
                else:
                    break
                value2 *= y
            if value1 > bound:
                break
            value1 *= x
        return list(res)
