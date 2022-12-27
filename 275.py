"""
@Author      :   Discount 
@Time        :   25/12/2022 15:05:29
@Description :   
"""

# 1739. Building Boxes
# 困难

# You have a cubic storeroom where the width, length, and height of the room are all equal to n units. You are asked to place n boxes in this room where each box is a cube of unit side length. There are however some rules to placing the boxes:

# You can place the boxes anywhere on the floor.
# If box x is placed on top of the box y, then each side of the four vertical sides of the box y must either be adjacent to another box or to a wall.
# Given an integer n, return the minimum possible number of boxes touching the floor.

# Example 1:
# Input: n = 3
# Output: 3
# Explanation: The figure above is for the placement of the three boxes.
# These boxes are placed in the corner of the room, where the corner is on the left side.

# Example 2:
# Input: n = 4
# Output: 3
# Explanation: The figure above is for the placement of the four boxes.
# These boxes are placed in the corner of the room, where the corner is on the left side.


# Example 3:
# Input: n = 10
# Output: 6
# Explanation: The figure above is for the placement of the ten boxes.
# These boxes are placed in the corner of the room, where the corner is on the back side.

# \sum_i i(i+1)/2 = 1/6 n(n+1)(n+2)

class Solution:
    def minimumBoxes(self, n: int) -> int:
        ans = max_n = 0
        i = j = 1
        while max_n + ans + i <= n:
            ans += i
            max_n += ans
            i += 1
        while max_n < n:
            ans += 1
            max_n += j
            j += 1
        return ans

test = Solution()

n=100

test.minimumBoxes(n)

#  直接计算

from math import ceil

class Solution:
    def minimumBoxes(self, n: int) -> int:
        x = int((6 * n) ** (1 / 3))
        ans = x * (x + 1) // 2
        max_n = x * (x + 1) * (x + 2) // 6
        if max_n > n:
            max_n -= ans
            ans -= x
        return ans + ceil((-1 + (1 + 8 * (n - max_n)) ** 0.5) / 2)

