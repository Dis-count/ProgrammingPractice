# 863. All Nodes Distance K in Binary Tree
# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
#
# You can return the answer in any order.
#
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
#
# Example 2:
#
# Input: root = [1], target = 1, k = 3
# Output: []
#
# （一）建图+bfs波纹法
# 这是最简单的思路。
# 1.完善好邻接表。
# 2.中心扩散

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #----------------- 当成图，构建邻接表中尚未构建的部分。---------------------#
        node_parent = dict()

        def dfs_find_parent(node: TreeNode) -> None:
            if node:
                if node.left:
                    node_parent[node.left] = node
                if node.right:
                    node_parent[node.right] = node
                dfs_find_parent(node.left)
                dfs_find_parent(node.right)

        dfs_find_parent(root)

        #---------------- bfs波纹法， 先visit&先判适应于距离大于1

        #---- k == 0
        if k == 0:
            return [target.val]

        res = []

        Q = collections.deque()
        visited = set()
        Q.append(target)
        visited.add(target)         #先visit
        level = 0
        while Q and level < k:
            level += 1
            for _ in range(len(Q)):
                x = Q.popleft()
                for y in [node_parent[x] if x in node_parent else None, x.left, x.right]:
                    if y and y not in visited:
                        if level == k:
                            res.append(y.val)       #先判
                        Q.append(y)
                        visited.add(y)

        return res
