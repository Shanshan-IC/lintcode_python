"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def sortList(self, head):
        if not head or not head.next:
            return head
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(mid)
        res = self.merge(l, r)
        return res

    def merge(self, l, r):
        if not l:
            return r
        if not r:
            return l
        res = None
        if l.val < r.val:
            res = l
            l = l.next
        else:
            res = r
            r = r.next
        tmp = res
        while l and r:
            if l.val < r.val:
                tmp.next = l
                l, tmp = l.next, tmp.next
            else:
                tmp.next = r
                r, tmp = r.next, tmp.next
        if l:
            tmp.next = l
        if r:
            tmp.next = r
        return res