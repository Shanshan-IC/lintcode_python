"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        maxs = -(1 << 31)
        _, maxs = self.helper(root, maxs)
        return maxs

    def helper(self, root, maxs):
        if not root:
            return 0, maxs
        left, maxs = self.helper(root.left, maxs)
        right, maxs = self.helper(root.right, maxs)
        sum1 = max(max(root.val + left, root.val + right), root.val)
        sum2 = max(sum1, left + right + root.val)
        maxs = max(maxs, sum2)
        return sum1, maxs