"""
@Author      :   Discount 
@Time        :   04/12/2022 11:28:37
@Description :   
"""

# 1774. Closest Dessert Cost
# 中等

# You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors and m types of toppings to choose from. You must follow these rules when making your dessert:

# There must be exactly one ice cream base.
# You can add one or more types of topping or have no toppings at all.
# There are at most two of each type of topping.
# You are given three inputs:

# baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
# toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
# target, an integer representing your target price for dessert.
# You want to make a dessert with a total cost as close to target as possible.

# Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.


# Example 1:
# Input: baseCosts = [1, 7], toppingCosts = [3, 4], target = 10
# Output: 10
# Explanation: Consider the following combination(all 0-indexed):
# - Choose base 1: cost 7
# - Take 1 of topping 0: cost 1 x 3 = 3
# - Take 0 of topping 1: cost 0 x 4 = 0
# Total: 7 + 3 + 0 = 10.

# Example 2:
# Input: baseCosts = [2, 3], toppingCosts = [4, 5, 100], target = 18
# Output: 17
# Explanation: Consider the following combination(all 0-indexed):
# - Choose base 1: cost 3
# - Take 1 of topping 0: cost 1 x 4 = 4
# - Take 2 of topping 1: cost 2 x 5 = 10
# - Take 0 of topping 2: cost 0 x 100 = 0
# Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.

# Example 3:
# Input: baseCosts = [3, 10], toppingCosts = [2, 5], target = 9
# Output: 8
# Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.

# M1 回溯
from typing import List

class Solution0:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = min(baseCosts)
        def dfs(p: int, cur_cost: int) -> None:
            nonlocal ans
            if abs(ans - target) < cur_cost - target:
                return
            if abs(ans - target) >= abs(cur_cost - target):
                if abs(ans - target) > abs(cur_cost - target):
                    ans = cur_cost
                else:
                    ans = min(ans, cur_cost)
            if p == len(toppingCosts):
                return
            dfs(p + 1, cur_cost + toppingCosts[p] * 2)
            dfs(p + 1, cur_cost + toppingCosts[p])
            dfs(p + 1, cur_cost)
        for c in baseCosts:
            dfs(0, c)
        return ans

# 时间复杂度：O(n×3^m)，其中 n，m 分别为数组 baseCosts，toppingCosts 的长度。
# 空间复杂度：O(m)，主要为回溯递归的空间开销。

# M2 动态规划  背包同时考虑 大于容量的选择

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        x = min(baseCosts)
        if x > target:
            return x
        can = [False] * (target + 1)
        ans = 2 * target - x
        for c in baseCosts:
            if c <= target:
                can[c] = True
            else:
                ans = min(ans, c)
        for c in toppingCosts:
            for count in range(2):
                for i in range(target, 0, -1):
                    if can[i] and i + c > target:
                        ans = min(ans, i + c)
                    if i - c > 0 and not can[i]:
                        can[i] = can[i - c]
        for i in range(ans - target + 1):
            if can[target - i]:
                return target - i
        return ans

