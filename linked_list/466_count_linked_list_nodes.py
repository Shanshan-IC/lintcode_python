"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        res = 0
        while (head):
            res += 1
            head = head.next
        return res