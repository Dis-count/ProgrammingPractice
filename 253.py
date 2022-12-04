"""
@Author      :   Discount 
@Time        :   02/12/2022 10:35:47
@Description :   
"""
# 1769. Minimum Number of Operations to Move All Balls to Each Box
# 中等


# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

# Each answer[i] is calculated considering the initial state of the boxes.

# Example 1:

# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

# Example 2:

# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]

# M1  two loops

from typing import List

class Solution1:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            s = sum(abs(j - i) for j, c in enumerate(boxes) if c == '1')
            res.append(s)
        return res

test = Solution1()


#  use the result from the last one
# update num_operations, num_left, num_right at each position.

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left, right, operations = int(boxes[0]), 0, 0
        for i in range(1, len(boxes)):
            if boxes[i] == '1':
                right += 1
                operations += i
        res = [operations]
        for i in range(1, len(boxes)):
            operations += left - right
            if boxes[i] == '1':
                left += 1
                right -= 1
            res.append(operations)
        return res



