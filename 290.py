# 2185. Counting Words With a Given Prefix
# 简单

# You are given an array of strings words and a string pref.

# Return the number of strings in words that contain pref as a prefix.

# A prefix of a string s is any leading contiguous substring of s.


# Example 1:
# Input: words = ["pay", "attention", "practice", "attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

# Example 2:
# Input: words = ["leetcode", "win", "loops", "success"], pref = "code"
# Output: 0
# Explanation: There are no strings that contain "code" as a prefix.


from typing import List

class Solution0:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)


words = ["pay", "attention", "practice", "attend"]

pref = "at"

test = Solution0()

test.prefixCount(words, pref)
