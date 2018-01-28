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
    @return: The head of linked list.
    """

    def insertionSortList(self, head):
        dummy = ListNode(0)
        while head:
            tmp = dummy
            next = head.next
            while tmp.next and tmp.next.val < head.val:
                tmp = tmp.next
            head.next = tmp.next
            tmp.next = head
            head = next
        return dummy.next


