# 1713. Minimum Operations to Make a Subsequence
# You are given an array target that consists of distinct integers and another integer array arr that can have duplicates.
#
# In one operation, you can insert any integer at any position in arr. For example, if arr = [1,4,1,2], you can add 3 in the middle and make it [1,4,3,1,2]. Note that you can insert the integer at the very beginning or end of the array.
#
# Return the minimum number of operations needed to make target a subsequence of arr.
#
# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.
#
#
# Example 1:
#
# Input: target = [5,1,3], arr = [9,4,2,3,4]
# Output: 2
# Explanation: You can add 5 and 1 in such a way that makes arr = [5,9,4,1,2,3,4], then target will be a subsequence of arr.
#
# Example 2:
#
# Input: target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
# Output: 3

# 最长公共子序列  但是复杂度超出  利用哈希表记录下标对应关系
# 结合 最长递增子序列

from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # 分析:
        # 本题要找最少操作次数，实际上就是找最长的公共子序列(这样需要的操作最少)
        # 根据target中互不相同，我们知道每个数字对应的坐标唯一
        # 于是最长公共子序列等价于arr用target的坐标转换后构成最长的上升子序列

        # 数字对应坐标
        idx_dict = {num: i for i, num in enumerate(target)}
        # 300.最长上升子序列
        stack = []
        for num in arr:
            # 只有在target的数字才可能属于公共子序列
            if num in idx_dict:
                # 转换坐标
                idx = idx_dict[num]
                # 该坐标在当前栈中的位置
                i = bisect.bisect_left(stack, idx)
                # 如果在最后要加入元素，否则要修改该位置的元素
                # 跟一般的讲，i代表了目前这个idx在stack中的大小位置，
                # 在前面出现还比idx大的stack中的元素是无法和idx构成最长上升子序列的。
                # i左边的数比idx小，可以和idx构成上升子序列，(idx构成的长度就是i+1)
                # idx比i的值小，将i替换后可以方便后面构成更优的子序列(越小后面能加入的数越多)
                if i == len(stack):
                    stack.append(0)
                stack[i] = idx
        # 最终stack的长度就构成了最长上升子序列的长度，用减法即可得到本题答案
        return len(target) - len(stack)
