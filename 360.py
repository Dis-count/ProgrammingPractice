# 834. Sum of Distances in Tree
# 困难

# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

# Example 1:
# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.

# Example 2:
# Input: n = 1, edges = []
# Output: [0]

# Example 3:
# Input: n = 2, edges = [[1,0]]
# Output: [1,1]

from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]  # g[x] 表示 x 的所有邻居
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = [0] * n
        size = [1] * n  # 注意这里初始化成 1 了，下面只需要累加儿子的子树大小
        def dfs(x: int, fa: int, depth: int) -> None:
            ans[0] += depth  # depth 为 0 到 x 的距离
            for y in g[x]:  # 遍历 x 的邻居 y
                if y != fa:  # 避免访问父节点
                    dfs(y, x, depth + 1)  # x 是 y 的父节点
                    size[x] += size[y]  # 累加 x 的儿子 y 的子树大小
        dfs(0, -1, 0)  # 0 没有父节点

        def reroot(x: int, fa: int) -> None:
            for y in g[x]:  # 遍历 x 的邻居 y
                if y != fa:  # 避免访问父节点
                    ans[y] = ans[x] + n - 2 * size[y]
                    reroot(y, x)  # x 是 y 的父节点
        reroot(0, -1)  # 0 没有父节点
        return ans