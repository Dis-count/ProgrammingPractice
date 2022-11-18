# 779. K-th Symbol in Grammar
# We build a table of n rows(1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth(1-indexed) symbol in the nth row of a table of n rows.

# Example 1:

# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0

# Example 2:

# Input: n = 2, k = 1
# Output: 0
# Explanation:
# row 1: 0
# row 2: 01

# Example 3:

# Input: n = 2, k = 2
# Output: 1
# Explanation:
# row 1: 0
# row 2: 01

# 我们可以注意到规律：每一行的后半部分正好为前半部分的“翻转”——前半部分是 0 后半部分变为 1，前半部分是 1，后半部分变为 0。且每一行的前半部分和上一行相同。我们可以通过「数学归纳法」来进行证明。

# 有了这个性质，那么我们再次思考原问题：对于查询某一个行第 k 个数字，如果 k 在后半部分，那么原问题就可以转化为求解该行前半部分的对应位置的“翻转”数字，又因为该行前半部分与上一行相同，所以又转化为上一行对应对应的“翻转”数字。那么按照这样一直递归下去，并在第一行时返回数字 0 即可。

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        if k > (1 << (n - 2)):
            return 1 ^ self.kthGrammar(n - 1, k - (1 << (n - 2)))
        return self.kthGrammar(n - 1, k)


# 时间复杂度：O(n)，其中 n 为题目给定表的行数。
# 空间复杂度：O(n)，其中 n 为题目给定表的行数，主要为递归的空间开销。

#  寻找翻转次数 = (k-1) 二进制个数
# 如果“翻转”为偶数次则原问题求解为 0，否则为 1。

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # return (k - 1).bit_count() & 1
        k -= 1
        res = 0
        while k:
            k &= k - 1
            res ^= 1
        return res
