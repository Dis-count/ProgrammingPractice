# 856. Score of Parentheses
# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.


# Example 1:

# Input: s = "()"
# Output: 1

# Example 2:

# Input: s = "(())"
# Output: 2

# Example 3:

# Input: s = "()()"
# Output: 2

# 栈

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for c in s:
            if c == '(':
                st.append(0)
            else:
                v = st.pop()
                st[-1] += max(2 * v, 1)
            print(st)
        return st[-1]


s = "()()"
ss = Solution()
ss.scoreOfParentheses(s)

# 时间复杂度：O(n)，其中 n 是字符串的长度。
# 空间复杂度：O(n)。栈需要 O(n) 的空间。

# 直接计算

# class Solution:
#     def scoreOfParentheses(self, s: str) -> int:
#         ans = bal = 0
#         for i, c in enumerate(s):
#             bal += 1 if c == '(' else -1
#             if c == ')' and s[i - 1] == '(':
#                 ans += 1 << bal
#         return ans


# 时间复杂度：O(n)，其中 n 是字符串的长度。
# 空间复杂度：O(1)。
