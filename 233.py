# 886. Possible Bipartition
# We want to split a group of n people(labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.


# Example 1:

# Input: n = 4, dislikes = [[1, 2], [1, 3], [2, 4]]
# Output: true
# Explanation: group1[1, 4] and group2[2, 3].

# Example 2:

# Input: n = 3, dislikes = [[1, 2], [1, 3], [2, 3]]
# Output: false

# Example 3:

# Input: n = 5, dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
# Output: false

# 深度优先

# 我们可以尝试用「染色法」来解决问题：假设第一组中的人是红色，第二组中的人为蓝色。我们依次遍历每一个人，如果当前的人没有被分组，就将其分到第一组（即染为红色），那么这个人不喜欢的人必须分到第二组中（染为蓝色）。然后任何新被分到第二组中的人，其不喜欢的人必须被分到第一组，依此类推。如果在染色的过程中存在冲突，就表示这个任务是不可能完成的，否则说明染色的过程有效（即存在合法的分组方案）。

from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        color = [0] * n  # color[x] = 0 表示未访问节点 x
        def dfs(x: int, c: int) -> bool:
            color[x] = c
            return all(color[y] != c and (color[y] or dfs(y, -c)) for y in g[x])
        return all(c or dfs(i, 1) for i, c in enumerate(color))

# 广度优先
from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        color = [0] * n  # color[x] = 0 表示未访问节点 x
        for i, c in enumerate(color):
            if c == 0:
                q = deque([i])
                color[i] = 1
                while q:
                    x = q.popleft()
                    for y in g[x]:
                        if color[y] == color[x]:
                            return False
                        if color[y] == 0:
                            color[y] = -color[x]
                            q.append(y)
        return True
