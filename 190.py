# 138. Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
#
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
#
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
#
# Return the head of the copied linked list.
#
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.
#
#
# Example 1:
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
# Example 2:
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
# Example 3:
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
# Example 4:
#
# Input: head = []
# Output: []
# Explanation: The given linked list is empty (null pointer), so return null.

#  新指针接在后面，复制、分离 A->A'->B->B'->C->C'->...
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        # 第一步，在每个原节点后面创建一个新节点
        # 1->1'->2->2'->3->3'
        while p:
            new_node = Node(p.val,None,None)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next
        p = head
        # 第二步，设置新节点的随机节点
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        # 第三步，将两个链表分离
        p = head
        dummy = Node(-1,None,None)
        cur = dummy
        while p:
            cur.next = p.next
            cur = cur.next
            p.next = cur.next
            p = p.next
        return dummy.next

#  哈希表  上下复制
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        # 创建一个哈希表，key 是原节点，value 是新节点
        d = dict()
        p = head
        # 将原节点和新节点放入哈希表中
        while p:
            new_node = Node(p.val,None,None)
            d[p] = new_node
            p = p.next
        p = head
        # 遍历原链表，设置新节点的next和random
        while p:
            # p是原节点，d[p]是对应的新节点，p.next是原节点的下一个
            # d[p.next]是原节点下一个对应的新节点
            if p.next:
                d[p].next = d[p.next]
            # p.random是原节点随机指向
            # d[p.random]是原节点随机指向  对应的新节点
            if p.random:
                d[p].random = d[p.random]
            p = p.next
        # 返回头结点，即原节点对应的value(新节点)
        return d[head]
