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
    @return: nothing
    """
    def reorderList(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        slow.next = None
        reversed = self.reverse(tmp)
        pos = head
        while pos:
            if not reversed:
                break
            r = reversed.next
            reversed.next = pos.next
            pos.next = reversed
            pos = pos.next.next
            reversed = r
        return head


    def reverse(self, head):
        if not head or not head.next:
            return head
        p = head
        q = head.next
        head.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        return p
