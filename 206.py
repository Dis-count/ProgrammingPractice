# 223. Rectangle Area
# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

# The first rectangle is defined by its bottom-left corner(ax1, ay1) and its top-right corner(ax2, ay2).

# The second rectangle is defined by its bottom-left corner(bx1, by1) and its top-right corner(bx2, by2).


# Example 1:
# Rectangle Area
# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# Output: 45

# Example 2:
# Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
# Output: 16

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlapWidth = min(ax2, bx2) - max(ax1, bx1)
        overlapHeight = min(ay2, by2) - max(ay1, by1)
        overlapArea = max(overlapWidth, 0) * max(overlapHeight, 0)
        return area1 + area2 - overlapArea

# 重叠部分的水平边投影到 x 轴上的线段为 [\max(\textit{ax}_1, \textit{bx}_1), \min(\textit{ax}_2, \textit{bx}_2)]，竖直边投影到 y 轴上的线段为[\max(\textit{ay}_1, \textit{by}_1), \min(\textit{ay}_2, \textit{by}_2)]
