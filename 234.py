# 904. Fruit Into Baskets
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the i-th tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree(including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# Example 1:

# Input: fruits = [1, 2, 1]
# Output: 3
# Explanation: We can pick from all 3 trees.

# Example 2:

# Input: fruits = [0, 1, 2, 2]
# Output: 3
# Explanation: We can pick from trees[1, 2, 2].
# If we had started at the first tree, we would only pick from trees[0, 1].

# Example 3:

# Input: fruits = [1, 2, 3, 2, 2]
# Output: 4
# Explanation: We can pick from trees[2, 3, 2, 2].
# If we had started at the first tree, we would only pick from trees[1, 2].

from typing import List
from collections import Counter

# 滑动窗口

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = Counter()

        left = ans = 0
        for right, x in enumerate(fruits):
            cnt[x] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans

# 时间复杂度：O(n)，其中 n 是数组 fruits 的长度。

# 空间复杂度：O(1)。哈希表中最多会有三个键值对，可以看成使用了常数级别的空间。
