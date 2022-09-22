# 1624. Largest Substring Between Two Equal Characters
# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.

# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".

# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.

#  直接遍历
#  字典 the key point is record the location when letters first appear.

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        firstIndex = {}
        for i, c in enumerate(s):
            if c not in firstIndex:
                firstIndex[c] = i
            else:
                ans = max(ans, i - firstIndex[c] - 1)
        return ans

# 复杂度分析

# 时间复杂度：O(n)，其中 n 表示字符串的长度。我们只需遍历一遍字符串即可。

# 空间复杂度：O(∣Σ∣)，其中 Σ 是字符集，在本题中字符集为所有小写字母，∣Σ∣=26。

s = Solution()
sss = 'aaa'
res = s.maxLengthBetweenEqualCharacters(sss)
print(res)
