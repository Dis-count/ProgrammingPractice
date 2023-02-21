# 1792. Maximum Average Pass Ratio
# 中等

# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.


# Example 1:
# Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# Output: 0.78333
# Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

# Example 2:
# Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
# Output: 0.53485


#  增加的通过率 递减 -> 贪心 使用优先队列

# 我们按照上述比较规则将每个班级放入优先队列中，进行 extraStudents 次操作。每一次操作，我们取出优先队列的堆顶元素，令其 pass 和 total 分别加 1，然后再放回优先队列。

# 最后我们遍历优先队列的每一个班级，计算其平均通过率即可得到答案。

from typing import List
from heapq import heapify, heapreplace

class Entry:
    __slots__ = 'p', 't'

    def __init__(self, p: int, t: int):
        self.p = p
        self.t = t

    def __lt__(self, b: 'Entry') -> bool:
        return (self.t - self.p) * b.t * (b.t + 1) > (b.t - b.p) * self.t * (self.t + 1)


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [Entry(*c) for c in classes]
        heapify(h)
        for _ in range(extraStudents):
            heapreplace(h, Entry(h[0].p + 1, h[0].t + 1))
        return sum(e.p / e.t for e in h) / len(h)
