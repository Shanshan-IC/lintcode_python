"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """

    def swapNodes(self, head, v1, v2):
        if head is None:
            return head
        dummy = ListNode(0, head)
        pre1, pre2 = self.findPrev(dummy, v1, v2)
        if pre1 is None or pre2 is None or pre1 == pre2:
            return head
        elif pre1.next == pre2:
            self.swapAdjcent(pre1)
        elif pre2.next == pre1:
            self.swapAdjcent(pre2)
        else:
            self.swapRemote(pre1, pre2)
        return dummy.next

    def findPrev(self, head, v1, v2):
        pre1, pre2 = None, None
        tmp = head
        while tmp.next:
            if tmp.next.val == v1:
                pre1 = tmp
            if tmp.next.val == v2:
                pre2 = tmp
            tmp = tmp.next
        return pre1, pre2

    def swapAdjcent(self, prev):
        node1 = prev.next
        node2 = node1.next
        post = node2.next

        prev.next = node2
        node2.next = node1
        node1.next = post

    def swapRemote(self, prev1, prev2):
        node1 = prev1.next
        post1 = node1.next

        node2 = prev2.next
        post2 = node2.next

        prev1.next = node2
        node2.next = post1

        prev2.next = node1
        node1.next = post2
