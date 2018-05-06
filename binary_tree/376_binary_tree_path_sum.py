"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    res = []

    def binaryTreePathSum(self, root, target):
        self.dfs(root, target, [])
        return self.res

    def dfs(self, root, target, ret):
        if root is None:
            return
        ret.append(root.val)
        target -= root.val
        if target == 0 and root.left is None and root.right is None:
            self.res.append(list(ret))
        else:
            self.dfs(root.left, target, ret)
            self.dfs(root.right, target, ret)
        ret.pop()