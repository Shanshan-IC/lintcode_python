"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None
        l, r = 0, len(lists) - 1
        return self.helper(lists, l, r)

    def helper(self, lists, l, r):
        if l == r:
            return lists[l]
        elif l + 1 == r:
            return self.mergeTwoLists(lists[l], lists[r])
        m = l + (r - l) / 2
        left = self.helper(lists, l, m)
        right = self.helper(lists, m + 1, r)
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        ans = ListNode(0)
        res = ans
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
        if l1:
            res.next = l1
        if l2:
            res.next = l2
        return ans.next