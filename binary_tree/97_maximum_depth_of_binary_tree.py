"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        if not root:
            return 0
        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)
        return max(l, r)