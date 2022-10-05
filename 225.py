# 811. Subdomain Visit Count
# A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.

# Example 1:

# Input: cpdomains = ["9001 discuss.leetcode.com"]
# Output: ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]
# Explanation: We only have one website domain: "discuss.leetcode.com".
# As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

# Example 2:

# Input: cpdomains = ["900 google.mail.com",
#                     "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: ["901 mail.com", "50 yahoo.com", "900 google.mail.com",
#          "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"]
# Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
# For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

# 为了获得每个子域名的计数配对域名，需要使用哈希表记录每个子域名的计数。遍历数组 cpdomains，对于每个计数配对域名，获得计数和完整域名，更新哈希表中的每个子域名的访问次数。

# 遍历数组 cpdomains 之后，遍历哈希表，对于哈希表中的每个键值对，关键字是子域名，值是计数，将计数和子域名拼接得到计数配对域名，添加到答案中。

from typing import List
from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = Counter()
        for domain in cpdomains:
            c, s = domain.split()
            c = int(c)
            cnt[s] += c
            while '.' in s:
                s = s[s.index('.') + 1:]
                cnt[s] += c
        return [f"{c} {s}" for s, c in cnt.items()]


# 复杂度分析

# 时间复杂度：O(L)，其中 L 是数组 cpdomains 中的所有字符串长度之和。遍历数组中所有的计数配对域名计算每个子域名的计数需要 O(L) 的时间，遍历哈希表也需要 O(L) 的时间。

# 空间复杂度：O(L)，其中 L 是数组 cpdomains 中的所有字符串长度之和。哈希表需要 O(L) 的空间。

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
s = Solution()
s.subdomainVisits(cpdomains)