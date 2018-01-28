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
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        res = ListNode(0, head)
        tmp = res
        while tmp.next and tmp.next.next:
            if tmp.next.val == tmp.next.next.val:
                prev = tmp.next.val
                while tmp.next and tmp.next.val == prev:
                    tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return res.next
