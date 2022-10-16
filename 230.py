# 1790. Check if One String Swap Can Make Strings Equal
# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string(not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

# Example 1:

# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".

# Example 2:

# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.

# Example 3:

# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.

#  计数统计

# 如果两个字符串 s_1,s_2相等，则不需要进行交换即可满足相等；
# 如果两个字符串 s_1,s_2不相等，字符串一定存在两个位置 i,j 处的字符不相等，需要交换 i,j 处字符使其相等，此时一定满足 s_1[i] = s_2[j], s_1[j] = s_2[i]；如果两个字符中只存在一个或大于两个位置的字符不相等，则此时无法通过一次交换使其相等；

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i = j = -1
        for idx, (x, y) in enumerate(zip(s1, s2)):
            if x != y:
                if i < 0:
                    i = idx
                elif j < 0:
                    j = idx
                else:
                    return False
        return i < 0 or j >= 0 and s1[i] == s2[j] and s1[j] == s2[i]


# 时间复杂度：O(n)，其中 n 表示字符串的长度。我们只需遍历一遍字符串即可。

# 空间复杂度：O(C)。由于两个字符串中字符不同的数目大于 2 即可返回，因此最多只需要保存 C = 2 个不同位置的索引即可。
s1 = "bank"

s2 = "kanb"