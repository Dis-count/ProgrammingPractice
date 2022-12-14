<<<<<<< HEAD
"""
@Author      :   Discount 
@Time        :   12/12/2022 11:56:44
@Description :   
"""

# 1781. Sum of Beauty of All Substrings
# 中等

# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.


# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

# Example 2:

# Input: s = "aabcbaa"
# Output: 17

# 双层循环， 遍历时维护更新用来记录字符频率的哈希表（字典）

from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            cnt = Counter()  # reset the count in the external loop
            mx = 0
            for j in range(i, len(s)):
                cnt[s[j]] += 1 # count the max and min in the internal loop
                mx = max(mx, cnt[s[j]])
                res += mx - min(cnt.values())
            
        return res

# 时间复杂度：O(C\times n^2)，其中 C 是 s 的元素种类，n 是 s 的长度。

# 空间复杂度：O(C)。

=======
# 1832. Check if the Sentence Is Pangram
# 简单

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false

class Solution0:
    def checkIfPangram(self, sentence: str) -> bool:
        exist = [False] * 26
        for c in sentence:
            exist[ord(c) - ord('a')] = True
        return all(exist)


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
>>>>>>> 95f5278e1273c8f2e5ca2c3e3fb266586b4275ef
