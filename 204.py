# 672. Bulb Switcher II
# There is a room with n bulbs labeled from 1 to n that all are turned on initially, and four buttons on the wall. Each of the four buttons has a different functionality where:

# Button 1: Flips the status of all the bulbs.
# Button 2: Flips the status of all the bulbs with even labels(i.e., 2, 4, ...).
# Button 3: Flips the status of all the bulbs with odd labels(i.e., 1, 3, ...).
# Button 4: Flips the status of all the bulbs with a label j = 3k + 1 where k = 0, 1, 2, ... (i.e., 1, 4, 7, 10, ...).
# You must make exactly presses button presses in total. For each press, you may pick any of the four buttons to press.

# Given the two integers n and presses, return the number of different possible statuses after performing all presses button presses.


# Example 1:

# Input: n = 1, presses = 1
# Output: 2
# Explanation: Status can be:
# - [off] by pressing button 1
# - [on] by pressing button 2
# Example 2:

# Input: n = 2, presses = 1
# Output: 3
# Explanation: Status can be:
# - [off, off] by pressing button 1
# - [on, off] by pressing button 2
# - [off, on] by pressing button 3
# Example 3:

# Input: n = 3, presses = 1
# Output: 4
# Explanation: Status can be:
# - [off, off, off] by pressing button 1
# - [off, on, off] by pressing button 2
# - [on, off, on] by pressing button 3
# - [off, on, on] by pressing button 4

class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        seen = set()
        for i in range(2**4):
            pressArr = [(i >> j) & 1 for j in range(4)]
            if sum(pressArr) % 2 == presses % 2 and sum(pressArr) <= presses:
                status = pressArr[0] ^ pressArr[1] ^ pressArr[3]
                if n >= 2:
                    status |= (pressArr[0] ^ pressArr[1]) << 1
                if n >= 3:
                    status |= (pressArr[0] ^ pressArr[2]) << 2
                if n >= 4:
                    status |= (pressArr[0] ^ pressArr[1] ^ pressArr[3]) << 3
                seen.add(status)
        return len(seen)


# 编号为 6k+1，受按钮 1, 3, 4 影响；
# 编号为 6k+2, 6k+6，受按钮 1, 2 影响；
# 编号为 6k+3, 6k+5，受按钮 1, 3 影响；
# 编号为 6k+4，受按钮 1, 2, 4 影响。
# 因此，只需要考虑四个灯泡，即可知道所有灯泡最后的状态了。

# 编写代码时，可以用一个长度为 4 数组 pressArr 表示 4 个按钮的按动情况。一个整数 status 表示四组灯泡亮灭的状态。最后计算遇到过几种不同的状态即可。

# In fact, you can also use three status to indicate the status.

#  Sol 2:

class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        elif n == 2:
            return 3 if presses == 1 else 4
        else:
            if presses == 1:
                return 4
            elif presses == 2:
                return 7
            else:
                return 8
