"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: T1: The roots of binary tree T1.
    @param: T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """

    def isSubtree(self, T1, T2):
        if T2 is None:
            return True
        if T1 is None:
            return False
        flag = False
        if T1.val == T2.val:
            flag = self.helper(T1, T2)
        if not flag:
            flag = self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
        return flag

    def helper(self, T1, T2):
        if T1 is not None and T2 is not None and T1.val == T2.val:
            return self.helper(T1.left, T2.left) and self.helper(T1.right, T2.right)
        return T1 is None and T2 is None