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

