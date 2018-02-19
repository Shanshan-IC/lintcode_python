"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        if root is None:
            return "{}"
        q = [root]
        idx = 0
        while idx < len(q):
            if q[idx] is not None:
                q.append(q[idx].left)
                q.append(q[idx].right)
            idx += 1
        print('{%s}' % ','.join(str(node.val) if node is not None else '#' for node in q))
        while q[-1] is not None:
            q.pop()
            print('{%s}' % ','.join(str(node.val) if node is not None else '#' for node in q))
        return '{%s}' % ','.join(str(node.val) if node is not None else '#' for node in q)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """

    def deserialize(self, data):
        return
# write your code here

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

Solution().serialize(root)