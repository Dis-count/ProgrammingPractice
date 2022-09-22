# 1640. Check Array Formation Through Concatenation
# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

# Return true if it is possible to form the array arr from pieces. Otherwise, return false.

# Example 1:

# Input: arr = [15, 88], pieces = [[88], [15]]
# Output: true
# Explanation: Concatenate[15] then[88]

# Example 2:

# Input: arr = [49, 18, 16], pieces = [[16, 18, 49]]
# Output: false
# Explanation: Even though the numbers match, we cannot reorder pieces[0].

# Example 3:

# Input: arr = [91, 4, 64, 78], pieces = [[78], [4, 64], [91]]
# Output: true
# Explanation: Concatenate[91] then[4, 64] then[78]

# 哈希表
from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index = {p[0]: i for i, p in enumerate(pieces)}
        i = 0
        while i < len(arr):
            if arr[i] not in index:
                return False
            p = pieces[index[arr[i]]]
            if arr[i: i + len(p)] != p:
                return False
            i += len(p)
        return True


arr = [91, 4, 64, 78]
pieces = [[78], [4, 64], [91]]

s = Solution()
s.canFormArray(arr, pieces)

# 复杂度分析

# 时间复杂度：O(n)，其中 n 是数组 arr 的长度。

# 空间复杂度：O(n)。保存哈希表需要 O(n) 的空间。
