# 2418. Sort the People
# 提示
# 简单

# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

 
# Example 1:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.

# Example 2:

# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        indices = list(range(n))
        indices.sort(key = lambda x: heights[x], reverse=True)
        res = []
        for i in indices:
            res.append(names[i])
        return res

names = ["Alice","Bob","Bob"]

heights = [155,185,150]

test = Solution()
test.sortPeople(names, heights)
