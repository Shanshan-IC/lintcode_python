"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        if root is None:
            return None
        root_cp = TreeNode(root.val)
        root_cp.left = self.cloneTree(root.left)
        root_cp.right = self.cloneTree(root.right)
        return root_cp
