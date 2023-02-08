# 1129. Shortest Path with Alternating Colors
# 中等

# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.


# Example 1:

# Input: n = 3, redEdges = [[0, 1], [1, 2]], blueEdges = []
# Output: [0, 1, -1]
# Example 2:

# Input: n = 3, redEdges = [[0, 1]], blueEdges = [[2, 1]]
# Output: [0, 1, -1]

# 广度优先 两种颜色同时搜索
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in redEdges:
            g[x].append((y, 0))
        for x, y in blueEdges:
            g[x].append((y, 1))
        
        dis = [-1] * n  # length of path from node 0 to node x 
        vis = {(0, 0), (0, 1)}  # from node 0 with two colors
        q = [(0, 0), (0, 1)]  # node, color
        level = 0
        while q:
            tmp = q
            q = []
            for x, color in tmp:
                if dis[x] == -1:  # update the obtained path
                    dis[x] = level
                for p in g[x]:
                    if p[1] != color and p not in vis: # find a new path
                        vis.add(p)
                        q.append(p)
            level += 1
        return dis

test = Solution()

n = 3

redEdges = [[0, 1]]

blueEdges = [[2, 1]]

test.shortestAlternatingPaths(n, redEdges, blueEdges)
