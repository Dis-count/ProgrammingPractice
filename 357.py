# 979. Distribute Coins in Binary Tree
# 中等

# You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

# In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

# Return the minimum number of moves required to make every node have exactly one coin.

# Example 1:

# Input: root = [3,0,0]
# Output: 2
# Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

# Example 2:

# Input: root = [0,3,0]
# Output: 3
# Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= n <= 100
# 0 <= Node.val <= n
# The sum of all Node.val is n.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def distributeCoins(self, root: Optional[TreeNode]) -> int:
#         ans = 0
#         def dfs(node: Optional[TreeNode]) -> (int, int):
#             if node is None:
#                 return 0, 0
#             coins_l, nodes_l = dfs(node.left)
#             coins_r, nodes_r = dfs(node.right)
#             coins = coins_l + coins_r + node.val  # 子树硬币个数
#             nodes = nodes_l + nodes_r + 1  # 子树节点数
#             nonlocal ans
#             ans += abs(coins - nodes)
#             return coins, nodes
#         dfs(root)
#         return ans

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            d = dfs(node.left) + dfs(node.right) + node.val - 1
            nonlocal ans
            ans += abs(d)
            return d
        dfs(root)
        return ans

test = Solution()

def construct_tree(values):
    if not values:
        return None
    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = construct_tree(values[:mid])
    root.right = construct_tree(values[mid+1:])
    return root

values = [1, 2, 3, 4, 5, 6, 7]
root = construct_tree(values)

# root = TreeNode(3,TreeNode(0),TreeNode(0))
# root = TreeNode(0,TreeNode(3),TreeNode(0))
# root = [0,3,0]

res = test.distributeCoins(root)
print(res)