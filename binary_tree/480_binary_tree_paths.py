"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if root is None:
            return []
        res = []
        self.dfs(root, res, [])
        return res

    def dfs(self, root, res, tmp):
        tmp.append(str(root.val))
        if root.left is None and root.right is None:
            res.append('->'.join(tmp))
            tmp.pop()
            return
        if root.left is not None:
            self.dfs(root.left, res, tmp)
        if root.right is not None:
            self.dfs(root.right, res, tmp)
        tmp.pop()