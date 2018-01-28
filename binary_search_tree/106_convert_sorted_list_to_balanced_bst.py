"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, A):
        tmp = []
        while A:
            tmp.append(A.val)
            A = A.next
        return self.sortedArrayToBST(tmp)

    def sortedArrayToBST(self, A):
        if not A:
            return None
        if len(A) == 0:
            return TreeNode(A[0])
        return self.help(A, 0, len(A) - 1)

    def help(self, A, l, r):
        if l > r:
            return None
        if l == r:
            return TreeNode(A[l])
        m = (l + r) / 2
        root = TreeNode(A[m])
        root.left = self.help(A, l, m - 1)
        root.right = self.help(A, m + 1, r)
        return root
