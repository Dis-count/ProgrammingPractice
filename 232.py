# 817. Linked List Components
# You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

# Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.


# Example 1:

# Input: head = [0, 1, 2, 3], nums = [0, 1, 3]
# Output: 2
# Explanation: 0 and 1 are connected, so[0, 1] and [3] are the two connected components.

# Example 2:

# Input: head = [0, 1, 2, 3, 4], nums = [0, 3, 1, 4]
# Output: 2
# Explanation: 0 and 1 are connected, 3 and 4 are connected, so[0, 1] and [3, 4] are the two connected components.


from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        numsSet = set(nums)
        inSet = False
        res = 0
        while head:
            if head.val not in numsSet:
                inSet = False
            elif not inSet:
                inSet = True
                res += 1
            head = head.next
        return res


# 时间复杂度：O(n)，需要遍历一遍链表。

# 空间复杂度：O(m)，其中 m 是数组 nums 的长度，需要一个哈希集合来存储 nums 的元素。

head = ListNode()
head.__init__([0, 1, 2, 3, 4])

nums = [0, 3, 1, 4]
s = Solution()

s.numComponents(head, nums)