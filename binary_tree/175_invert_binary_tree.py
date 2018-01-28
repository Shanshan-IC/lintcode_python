"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# recusion method

class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        if not root:
            return root
        right = root.right
        root.right = self.invertBinaryTree(root.left)
        root.left = self.invertBinaryTree(right)
        return root

# non-recursion
class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        if not root:
            return root
        q = [root]
        while q:
            front = q.pop(0)
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
            front.left, front.right = front.right, front.left
        return root
