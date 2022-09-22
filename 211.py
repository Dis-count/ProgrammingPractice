# 854. K-Similar Strings
# Strings s1 and s2 are k-similar(for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

# Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.


# Example 1:

# Input: s1 = "ab", s2 = "ba"
# Output: 1
# Example 2:

# Input: s1 = "abc", s2 = "bca"
# Output: 2


# Constraints:

# 1 <= s1.length <= 20
# s2.length == s1.length
# s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
# s2 is an anagram of s1.

# 1. 广度优先（对于当前的每一位，找到之后所有可以交换的）

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        step, n = 0, len(s1)
        q, vis = [(s1, 0)], {s1}
        while True:
            tmp = q
            q = []
            for s, i in tmp:
                if s == s2:
                    return step
                while i < n and s[i] == s2[i]:
                    i += 1
                for j in range(i + 1, n):
                    if s[j] == s2[i] != s2[j]:  # 剪枝，只在 s[j] != s2[j] 时去交换
                        t = list(s)
                        t[i], t[j] = t[j], t[i]
                        t = ''.join(t)
                        if t not in vis:
                            vis.add(t)
                            q.append((t, i + 1))
            step += 1

# 注意数据结构的选取

# 2. 深度优先（对于当前的一位， 找到一个可以交换的，移到下一位，继续找一个可以交换的）

