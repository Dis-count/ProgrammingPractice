# 855. Exam Room
# 中等

# There is an exam room with n seats in a single row labeled from 0 to n - 1.

# When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number 0.

# Design a class that simulates the mentioned exam room.

# Implement the ExamRoom class:

# ExamRoom(int n) Initializes the object of the exam room with the number of the seats n.
# int seat() Returns the label of the seat at which the next student will set.
# void leave(int p) Indicates that the student sitting at seat p will leave the room. It is guaranteed that there will be a student sitting at seat p.


# Example 1:

# Input
# ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
# [[10], [], [], [], [], [4], []]
# Output
# [null, 0, 9, 4, 2, null, 5]

# Explanation
# ExamRoom examRoom = new ExamRoom(10)
# examRoom.seat()
# // return 0, no one is in the room, then the student sits at seat number 0.
# examRoom.seat()
# // return 9, the student sits at the last seat number 9.
# examRoom.seat()
# // return 4, the student sits at the last seat number 4.
# examRoom.seat()
# // return 2, the student sits at the last seat number 2.
# examRoom.leave(4)
# examRoom.seat()
# // return 5, the student sits at the last seat number 5.


# https: // leetcode.cn/problems/exam-room/solutions/2037447/by-lcbin-tstp/
# 有序集合 + 哈希表

from sortedcontainers import SortedList

class ExamRoom:

    def __init__(self, n: int):
        def dist(x):
            l, r = x
            return r - l - 1 if l == -1 or r == n else (r - l) >> 1

        self.n = n
        self.ts = SortedList(key=lambda x: (-dist(x), x[0]))
        self.left = {}
        self.right = {}
        self.add((-1, n))

    def seat(self) -> int:
        s = self.ts[0]
        p = (s[0] + s[1]) >> 1
        if s[0] == -1:
            p = 0
        elif s[1] == self.n:
            p = self.n - 1
        self.delete(s)
        self.add((s[0], p))
        self.add((p, s[1]))
        return p

    def leave(self, p: int) -> None:
        l, r = self.left[p], self.right[p]
        self.delete((l, p))
        self.delete((p, r))
        self.add((l, r))

    def add(self, s):
        self.ts.add(s)
        self.left[s[1]] = s[0]
        self.right[s[0]] = s[1]

    def delete(self, s):
        self.ts.remove(s)
        self.left.pop(s[1])
        self.right.pop(s[0])


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
