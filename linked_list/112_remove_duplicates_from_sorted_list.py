"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        pre = head
        while pre:
            while pre.next and pre.val == pre.next.val:
                pre.next = pre.next.next
            pre = pre.next
        return head