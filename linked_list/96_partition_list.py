"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        left, right = ListNode(0, head), ListNode(0, head)
        pre_l, pre_r = left, right
        while head:
            if head.val < x:
                pre_l.next = head
                pre_l = pre_l.next
            else:
                pre_r.next = head
                pre_r = pre_r.next
            head = head.next
        pre_r.next = None
        pre_l.next = right.next
        return left.next
