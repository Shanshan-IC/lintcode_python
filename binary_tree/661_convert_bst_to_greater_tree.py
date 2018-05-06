"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """

    def convertBST(self, root):
        self.sum = 0
        self.dfs(root)
        return root

    def dfs(self, root):
        if root is None:
            return
        if root.right:
            self.dfs(root.right)
        self.sum += root.val
        root.val = self.sum
        if root.left:
            self.dfs(root.left)
