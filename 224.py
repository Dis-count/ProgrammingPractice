# 921. Minimum Add to Make Parentheses Valid
# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB(A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# Example 1:

# Input: s = "())"
# Output: 1

# Example 2:

# Input: s = "((("
# Output: 3

# 对于括号匹配的题目，常用的做法是使用栈进行匹配，栈具有后进先出的特点，因此可以保证右括号和最近的左括号进行匹配。其实，这道题可以使用计数代替栈，进行匹配时每次都取距离当前位置最近的括号，就可以确保平衡。

# 从左到右遍历字符串，在遍历过程中维护左括号的个数以及添加次数。

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                ans += 1
        return ans + cnt

# cnt is the number of left
# 时间复杂度：O(n)，其中 n 是字符串的长度。遍历字符串一次。

# 空间复杂度：O(1)。只需要维护常量的额外空间。
