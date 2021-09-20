# 1736. Latest Time by Replacing Hidden Digits
# You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).
#
# The valid times are those inclusively between 00:00 and 23:59.
#
# Return the latest valid time you can get from time by replacing the hidden digits.
#
# Example 1:
#
# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
#
# Example 2:
#
# Input: time = "0?:3?"
# Output: "09:39"
# Example 3:
#
# Input: time = "1?:22"
# Output: "19:22"

class Solution:
    def maximumTime(self, time: str) -> str:
        atime = [str(z) for z in time]
        if time[0] == '?':
            if  '4' <= time[1] <= '9':
                atime[0] = '1'
            else:
                atime[0] = '2'
        if time[1] == '?':
            if time[0] =='?' or time[0] =='2':
                atime[1] = '3'
            else:
                atime[1] = '9'
        if time[3] == '?':
            atime[3] = '5'
        if time[4] == '?':
            atime[4] = '9'
        return ''.join(atime)

a = Solution()
time = "2?:?0"
a.maximumTime(time)

#
class Solution:
    def maximumTime(self, time: str) -> str:
        [a, b, _, c, d] = time
        if a == '?':
            a = '2' if b == '?' or b < '4' else '1'
        if b == '?':
            b = '3' if a == '2' else '9'
        if c == '?':
            c = '5'
        if d == '?':
            d = '9'
        return f'{a}{b}:{c}{d}'

time = "1?:22"
[a, b, _, c, d] = time
