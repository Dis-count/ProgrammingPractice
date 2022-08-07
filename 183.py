# 1104. Path In Zigzag Labelled Binary Tree
# In an infinite binary tree where every node has two children, the nodes are labelled in row order.
#
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.
#
# Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.
#
# Example 1:
#
# Input: label = 14
# Output: [1,3,4,14]
#
# Example 2:
#
# Input: label = 26
# Output: [1,2,6,10,26]

# 先假设原题从同一个方向标记数字，找出在此情况下路径的值
# 在从label开始，隔一行将需要翻转的数字翻转，最后输出所需答案

from typing import List

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        temp= label
        ans = []
        while temp:
            ans.append(temp)
            temp = temp//2
        n = len(ans)


        for i in range(n):
            if i%2==0:
                continue
            ans[i] = pow(2,n-i)+pow(2,n-i-1)-1-ans[i]
        ans.reverse()
        return ans
