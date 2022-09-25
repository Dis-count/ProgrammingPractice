# 707. Design Linked List
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 
# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3

#  单向链表

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index)
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next


# 时间复杂度：初始化消耗 O(1)，get 消耗 O(index)，addAtHead 消耗 O(1)，addAtTail 消耗 O(n)，其中 n 为链表当前长度，即 addAtHead，addAtTail 和 addAtIndex 已调用次数之和，addAtIndex 消耗 O(index)。

# 空间复杂度：所有函数的单次调用空间复杂度均为 O(1)，总体空间复杂度为 O(n)，其中 n 为 addAtHead，addAtTail 和 addAtIndex 调用次数之和。

myLinkedList = MyLinkedList()

myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    # linked list becomes 1->2->3
myLinkedList.get(1);              # return 2
myLinkedList.deleteAtIndex(1);    # now the linked list is 1->3
myLinkedList.get(1);              # return 3
