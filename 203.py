# 1619. Mean of Array After Removing Some Elements
# Given an integer array arr, return the mean of the remaining integers after removing the smallest 5 % and the largest 5 % of the elements.

# Answers within 10^{-5} of the actual answer will be considered accepted.

# Example 1:

# Input: arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
# Output: 2.00000
# Explanation: After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.
# Example 2:

# Input: arr = [6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]
# Output: 4.00000
# Example 3:

# Input: arr = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1,
#               2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4]
# Output: 4.77778


# Constraints:
# 20 <= arr.length <= 1000
# arr.length is a multiple of 20.
# 0 <= arr[i] <= 105



from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        return sum(arr[n // 20: -n // 20]) / (n * 0.9)

s = Solution()
arr = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 
2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4]
res = s.trimMean(arr)
print(res)

# 方法一：排序
# 设元素数目为 nn，我们先对整数数组 \textit{arr}arr 从小到大进行排序，然后对区间 \big[dfrac{n}{20}, \dfrac{19n}{20} \big) 内的元素进行求和，得到未删除元素的求和结果 \textit{partialSum}partialSum，返回均值 \dfrac{\textit{partialSum}}{0.9n}

# 时间复杂度：O(nlogn)，其中 n 是数组 arr 的长度。

# 空间复杂度：O(logn)。排序需要 O(logn) 的栈空间。

