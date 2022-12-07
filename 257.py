# 1805. Number of Different Integers in a String
# 简单

# You are given a string word that consists of digits and lowercase English letters.

# You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".

# Return the number of different integers after performing the replacement operations on word.

# Two integers are considered different if their decimal representations without any leading zeros are different.

# Example 1:
# Input: word = "a123bc34d8ef34"
# Output: 3
# Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.

# Example 2:
# Input: word = "leet1234code234"
# Output: 2

# Example 3:
# Input: word = "a1b01c001"
# Output: 1
# Explanation: The three integers "1", "01", and "001" all represent the same integer because
# the leading zeros are ignored when comparing their decimal values.

# 双指针

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        n = len(word)
        p1 = 0
        while True:
            while p1 < n and not word[p1].isdigit():
                p1 += 1
            if p1 == n:
                break
            p2 = p1
            while p2 < n and word[p2].isdigit():
                p2 += 1
            while p2 - p1 > 1 and word[p1] == '0':  # 去除前导 0
                p1 += 1
            s.add(word[p1:p2])
            p1 = p2
        return len(s)

# 时间复杂度：O(n)，其中 n 是字符串 word 的长度。
# 空间复杂度：O(n)。哈希集合需要占用 O(n) 的空间。
