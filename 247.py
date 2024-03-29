# 809. Expressive Words
# 中等
# Sometimes people repeat letters to represent extra feeling. For example:

# "hello" -> "heeellooo"
# "hi" -> "hiiii"
# In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

# You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
# Return the number of query strings that are stretchy.


# Example 1:

# Input: s = "heeellooo", words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

# Example 2:

# Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
# Output: 3

#  双指针
from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def expand(s: str, t: str) -> bool:
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    return False
                ch = s[i]
                cnti = 0
                while i < len(s) and s[i] == ch:
                    cnti += 1
                    i += 1
                cntj = 0
                while j < len(t) and t[j] == ch:
                    cntj += 1
                    j += 1
                
                if cnti < cntj:
                    return False
                if cnti != cntj and cnti < 3:
                    return False
            
            return i == len(s) and j == len(t)
        
        return sum(int(expand(s, word)) for word in words)


test = Solution()

