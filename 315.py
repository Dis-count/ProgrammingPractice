# 1234. Replace the Substring for Balanced String
# 中等

# You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

# A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

# Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.


# Example 1:
# Input: s = "QWER"
# Output: 0
# Explanation: s is already balanced.

# Example 2:
# Input: s = "QQWE"
# Output: 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

# Example 3:
# Input: s = "QQQW"
# Output: 2
# Explanation: We can replace the first "QQ" to "ER". 

# 'substring'
#  滑动窗口

from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        partial = len(s) // 4

        def check():
            if cnt['Q'] > partial or \
                    cnt['W'] > partial or \
                    cnt['E'] > partial or \
                    cnt['R'] > partial:
                return False
            return True

        if check():
            return 0

        res = len(s)
        r = 0
        for l, c in enumerate(s):
            while r < len(s) and not check():
                cnt[s[r]] -= 1
                r += 1
                print(r)
            if not check():
                break
            res = min(res, r - l)
            cnt[c] += 1
            print(cnt)
        return res

s = "QQWEQ"

test = Solution()
res = test.balancedString(s)
print(f'result: {res}')