"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        cur = None
        while head:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
        return cur
