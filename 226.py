# 927. Three Equal Parts
# You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

# If it is possible, return any[i, j] with i + 1 < j, such that:

# arr[0], arr[1], ..., arr[i] is the first part,
# arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
# arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
# All three parts have equal binary values.
# If it is not possible, return [-1, -1].

# Note that the entire part is used when considering what binary value it represents. For example, [1, 1, 0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so[0, 1, 1] and [1, 1] represent the same value.

# Example 1:

# Input: arr = [1, 0, 1, 0, 1]
# Output: [0, 3]

# Example 2:

# Input: arr = [1, 1, 0, 1, 1]
# Output: [-1, -1]

# Example 3:

# Input: arr = [1, 1, 0, 0, 1]
# Output: [0, 2]
from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        s = sum(arr)
        if s % 3:
            return [-1, -1]
        if s == 0:
            return [0, 2]

        partial = s // 3
        first = second = third = cur = 0
        for i, x in enumerate(arr):
            if x:
                if cur == 0:
                    first = i
                elif cur == partial:
                    second = i
                elif cur == 2 * partial:
                    third = i
                cur += 1

        n = len(arr)
        length = n - third
        if first + length <= second and second + length <= third:
            i = 0
            while third + i < n:
                if arr[first + i] != arr[second + i] or arr[first + i] != arr[third + i]:
                    return [-1, -1]
                i += 1
            return [first + length - 1, second + length]
        return [-1, -1]


# 时间复杂度：O(n)，其中 n 是 arr 的长度。找到三个下标的时间复杂度为 O(n)，判断三个部分是否相同的时间复杂度也是 O(n)。

# 空间复杂度：O(1)，只用到常数个变量空间。
