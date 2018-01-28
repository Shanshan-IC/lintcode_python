"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: l1: the first list
    @param: l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        m = 0
        res = ListNode(0)
        prev = res
        while l1 or l2 or m:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + m
            prev.next = ListNode(val % 10)
            m = val / 10
            prev = prev.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return res.next