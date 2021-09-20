# 274. H-Index
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.
#
# If there are several possible values for h, the maximum one is taken as the h-index.
#
#
# Example 1:
#
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
#
# Example 2:
#
# Input: citations = [1,3,1]
# Output: 1

# 直接根据定义 排序即可

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citation = sorted(citations, reverse = True)
        h = 0; i = 0; n = len(citations)
        while i < n and sorted_citation[i] > h:
            h += 1
            i += 1
        return h

# 时间复杂度：O(nlogn)，其中 n 为数组 citations 的长度。即为排序的时间复杂度。
# 空间复杂度：O(logn)，其中 n 为数组 citations 的长度。即为排序的空间复杂度。

#  计数排序
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations); tot = 0
        counter = [0] * (n+1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        # print(counter)
        for i in range(n, -1, -1):
            tot += counter[i]
            if tot >= i:
                return i
        return 0

citations = [3,0,6,1,5]
a = Solution()
a.hIndex(citations)
