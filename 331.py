# 1641. Count Sorted Vowel Strings
# 提示
# 中等

# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.


# Example 1:

# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

# Example 2:

# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

# Example 3:

# Input: n = 33
# Output: 66045


class Solution:
    def countVowelStrings(self, n: int) -> int:
        lis = [[1 for _ in range(5)] for _ in range(n+1)]
        for i in range(1,n+1,1):
            for j in range(5):
                lis[i][j] = sum(lis[i-1][j:5])
        return lis[n][0]

res = Solution()
res.countVowelStrings(33)


#  A better solution

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(n - 1):
            for j in range(1, 5):
                dp[j] += dp[j - 1]
        return sum(dp)

# The easiest solution

from math import comb

# C_{n+4}^{4}

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return comb(n + 4, 4)
