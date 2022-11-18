# 792. Number of Matching Subsequences
# 中等

# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".


# Example 1:

# Input: s = "abcde", words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

# Example 2:

# Input: s = "dsahjpjauf", words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
# Output: 2

# 朴素方法,逐个比较+ 二分

from bisect import bisect_right
from collections import defaultdict
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        ans = len(words)
        for w in words:
            if len(w) > len(s):
                ans -= 1
                continue
            p = -1
            for c in w:
                ps = pos[c]
                j = bisect_right(ps, p)
                if j == len(ps):
                    ans -= 1
                    break
                p = ps[j]
        return ans


s = "abcdeba"
words = ["a", "bb", "acd", "ace"]

test = Solution()
test.numMatchingSubseq(s, words)

# M2 多指针 同时匹配

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        p = defaultdict(list)
        for i, w in enumerate(words):
            p[w[0]].append((i, 0))
        ans = 0
        for c in s:
            q = p[c]
            p[c] = []
            for i, j in q:
                j += 1 # i is i-th element in words, j is the j-th char of the i-th word.
                if j == len(words[i]):
                    ans += 1
                else:
                    p[words[i][j]].append((i, j))
        return ans

test = Solution()
test.numMatchingSubseq(s, words)


