"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        if head == None:
            return head
        #  可能链表中的所有元素val都等于val，所以需要新增一个头节点
        newHead = ListNode(0)
        newHead.next = head
        head = newHead
        while (head.next):
            if (head.next.val == val):
                head.next = head.next.next
            else:
                head = head.next
        return newHead.next    