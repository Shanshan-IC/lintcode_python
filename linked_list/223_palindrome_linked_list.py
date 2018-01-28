"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: A ListNode.
    @return: A boolean.
    """

    def isPalindrome(self, head):
        q = []
        cur = head
        while cur:
            q.append(cur.val)
            cur = cur.next
        cur = head
        while cur:
            tmp = q.pop()
            if cur.val != tmp:
                return False
            cur = cur.next
        return True

