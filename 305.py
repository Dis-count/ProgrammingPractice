# 1145. Binary Tree Coloring Game
# 中等

# Two players play a turn based game on a binary tree. We are given the root of this binary tree, and the number of nodes n in the tree. n is odd, and each node has a distinct value from 1 to n.

# Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x. The first player colors the node with value x red, and the second player colors the node with value y blue.

# Then, the players take turns starting with the first player. In each turn, that player chooses a node of their color(red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node(either the left child, right child, or parent of the chosen node.)

# If (and only if) a player cannot choose such a node in this way, they must pass their turn. If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

# You are the second player. If it is possible to choose such a y to ensure you win the game, return true. If it is not possible, return false.


# Example 1:

# Input: root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], n = 11, x = 3
# Output: true
# Explanation: The second player can choose the node with value 2.

# Example 2:

# Input: root = [1, 2, 3], n = 3, x = 1
# Output: false

#  深度优先

# 二号玩家应选择节点数最多的区域中的一个节点着色。

# 为了判断二号玩家是否可以获胜，需要分别计算三个区域的节点数。如果存在一个区域的节点数不少于 (n+1)/2; 则二号玩家可以选择该区域着色并获胜
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        xNode = None

        def getSubtreeSize(node):
            if not node:
                return 0
            if node.val == x:
                nonlocal xNode
                xNode = node
            return 1 + getSubtreeSize(node.left) + getSubtreeSize(node.right)

        getSubtreeSize(root)
        leftSize = getSubtreeSize(xNode.left)
        if leftSize >= (n + 1) // 2:
            return True
        rightSize = getSubtreeSize(xNode.right)
        if rightSize >= (n + 1) // 2:
            return True
        remain = n - leftSize - rightSize - 1
        return remain >= (n + 1) // 2

