# 1140. Stone Game II
# 提示

# Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

# The game continues until all the stones have been taken.

# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.


# Example 1:
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

# Example 2:
# Input: piles = [1,2,3,4,5,100]
# Output: 104

from math import inf
from typing import List
from functools import lru_cache, cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        prefixSum = [0]
        for a in piles:
            prefixSum.append(prefixSum[-1] + a)
        
        @lru_cache(None)
        def dp(i, m):
            if i == len(piles):
                return 0
            mx = -inf
            for x in range(1, 2 * m + 1):                
                if i+x > len(piles):
                    break
                mx = max(mx, prefixSum[i + x] - prefixSum[i] - dp(i + x, max(m, x)))
            return mx
            
        return (prefixSum[-1]+dp(0, 1)) // 2

# 要求出爱丽丝可以得到的最大数量的石头，可以先求出爱丽丝最多比鲍勃多拿的石头数量，再经过计算得到爱丽丝最多可以得到的石头数量。而在两方都采取最优策略的情况下，求其中一方的得分，这种情况可以用记忆化搜索来解题。

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

factorial(9)

factorial.cache_info()