"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: the List
    @param: k: rotate to the right k places
    @return: the list after rotation
    """

    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        fast, slow = head, head
        l = 0
        while fast:
            l += 1
            fast = fast.next
        k %= l
        fast = head
        while k:
            fast = fast.next
            k -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
