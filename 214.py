# 1652. Defuse the Bomb
# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

# If k > 0, replace the i-th number with the sum of the next k numbers.
# If k < 0, replace the i-th number with the sum of the previous k numbers.
# If k == 0, replace the i-th number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

# Example 1:

# Input: code = [5, 7, 1, 4], k = 3
# Output: [12, 10, 16, 13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

# Example 2:

# Input: code = [1, 2, 3, 4], k = 0
# Output: [0, 0, 0, 0]
# Explanation: When k is zero, the numbers are replaced by 0.

# Example 3:

# Input: code = [2, 4, 9, 3], k = -2
# Output: [12, 5, 6, 13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

#  滑动窗口

# 只需要在从左往右遍历的过程中维护数组的和即可

from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        res = []
        n = len(code)
        code += code
        if k > 0:
            l, r = 1, k
        else:
            l, r = n + k, n - 1
        w = sum(code[l:r+1])
        for i in range(n):
            res.append(w)
            w -= code[l]
            w += code[r + 1]
            l, r = l + 1, r + 1
        return res

code = [5, 7, 1, 4]
k = 3
s = Solution()
s.decrypt(code,k)