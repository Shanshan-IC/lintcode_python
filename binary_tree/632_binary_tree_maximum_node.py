class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):
        if root is None:
            return root
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max(root, self.max(left, right))

    def max(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        if left.val > right.val:
            return left
        return right