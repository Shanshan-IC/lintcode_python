"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        pre = ListNode(0)
        pre.next = head
        tmp = pre
        while n:
            head = head.next
            n -= 1
        while head:
            tmp = tmp.next
            head = head.next
        tmp.next = tmp.next.next
        return pre.next

