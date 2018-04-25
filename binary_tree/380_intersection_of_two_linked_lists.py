"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        t1, t2 = headA, headB
        while t1 != t2:
            t1 = headB if t1 is None else t1.next
            t2 = headA if t2 is None else t2.next
        return t1
