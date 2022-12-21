# 1971. Find if Path Exists in Graph
# 简单

# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.


# Example 1:

# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Example 2:

# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.

#  广度优先

# 使用广度优先搜索判断顶点 source 到顶点 destination 的连通性，需要我们从顶点 source 开始按照层次依次遍历每一层的顶点，检测是否可以到达顶点 destination。遍历过程我们使用队列存储最近访问过的顶点，同时记录每个顶点的访问状态，每次从队列中取出顶点 vertex 时，将其未访问过的邻接顶点入队列。

# 初始时将顶点 source 设为已访问，并将其入队列。每次将队列中的节点 vertex 出队列，并将与 vertex 相邻且未访问的顶点 next 入队列，并将 next 设为已访问。当队列为空或访问到顶点 destination 时遍历结束，返回顶点 destination 的访问状态即可。


#  DFS
from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(i):
            if i == destination:
                return True
            vis.add(i)
            for j in g[i]:
                if j not in vis and dfs(j):
                    return True
            return False

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        vis = set()

        return dfs(source)

#  并查集

class Solution1:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        
        for u, v in edges:
            p[find(u)] = find(v)
            
        print(find(source))
        return find(source) == find(destination)


n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3], [2,3]]
source = 0
destination = 5

test = Solution1()
test.validPath(n, edges, source, destination)

