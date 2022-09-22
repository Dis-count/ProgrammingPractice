# 827. Making A Large Island
# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

# Example 1:

# Input: grid = [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

# Example 2:

# Input: grid = [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

# Example 3:

# Input: grid = [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.

# 方法一：标记岛屿 + 合并
# 我们给每个岛屿进行标记，标记值与岛屿的某个 grid[i][j] 有关，即 t = i×n+j+1，t 唯一。使用 tag 记录每个点所属的岛屿的标记，并且使用哈希表 area 保存每个岛屿的面积。岛屿的面积可以使用深度优先搜索或广度优先搜索计算。

# 对于每个 grid[i][j] = 0，我们计算将它变为 1 后，新合并的岛屿的面积 z（z 的初始值为 1，对应该点的面积）：使用集合 connected 保存与 grid[i][j] 相连的岛屿，遍历与 grid[i][j] 相邻的四个点，如果该点的值为 1，且它所在的岛屿并不在集合中，我们将 z 加上该点所在的岛屿面积，并且将该岛屿加入集合中。所有这些新合并岛屿以及原来的岛屿的面积的最大值就是最大的岛屿面积。
from typing import List
from collections import Counter

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tag = [[0] * n for _ in range(n)]
        area = Counter()
        def dfs(i: int, j: int) -> None:
            tag[i][j] = t
            area[t] += 1
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 四个方向
                if 0 <= x < n and 0 <= y < n and grid[x][y] and tag[x][y] == 0:
                    dfs(x, y)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x and tag[i][j] == 0:  # 枚举没有访问过的陆地
                    t = i * n + j + 1
                    dfs(i, j)
        ans = max(area.values(), default=0)

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:  # 枚举可以添加陆地的位置
                    new_area = 1
                    connected = {0}
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 四个方向
                        if 0 <= x < n and 0 <= y < n and tag[x][y] not in connected:
                            new_area += area[tag[x][y]]
                            connected.add(tag[x][y])
                    ans = max(ans, new_area)
        return ans

# 时间复杂度：O(n^2)，其中 n 是 grid 的长与宽。使用深度优先搜索获取岛屿面积时，总共访问不超过 n^2 个点。

# 空间复杂度：O(n^2)。保存 tag 与 area 需要 O(n^2) 的空间。


# 先BFS搜索所有现成的岛屿，并把每一个岛屿都标记上号码，同时统计出来面积，再枚举每一个值为0的块儿，四周联通计算

# sol2

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, count = len(grid), 2
        area = [0]*(n*n+5)  # 标记每个联通块儿的面积
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = count
                    lis, p = [[i, j]], 0
                    while p < len(lis):
                        a = lis[p]
                        for m in move:
                            x, y = a[0]+m[0], a[1]+m[1]
                            if x < 0 or x == n or y < 0 or y == n or grid[x][y] != 1:
                                continue
                            grid[x][y] = count
                            lis.append([x, y])
                        p += 1
                    area[count] = p
                    count += 1
        ans = 0
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    s = set()
                    for m in move:
                        x, y = i+m[0], j+m[1]
                        if x < 0 or x == n or y < 0 or y == n or not grid[x][y]:
                            continue
                        s.add(grid[x][y])
                    ans = max(ans, 1+sum(area[a] for a in s))
        return ans if ans else n*n
