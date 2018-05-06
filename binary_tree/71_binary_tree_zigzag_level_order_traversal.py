"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        self.res = []
        self.preorder(root, 0)
        return self.res

    def preorder(self, root, level):
        if root:
            if len(self.res) < level + 1:
                self.res.append([])
            if level & 1:
                self.res[level].insert(0, root.val)
            else:
                self.res[level].append(root.val)
            self.preorder(root.left, level + 1)
            self.preorder(root.right, level + 1)