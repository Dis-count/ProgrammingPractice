# 451. Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.
#
# Example 1:
#
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
#
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return "".join(v for v in sorted(c.keys(), key=lambda x:-c[x]) for i in range(c[v]))


#  Or

class Solution:
    def frequencySort(self, s):
        li = []
        for i, j in Counter(s).items():
            li.append([i, j])
        new_li = sorted(li, key=lambda x: -x[1])
        return ''.join([i * j for i,j in new_li])
