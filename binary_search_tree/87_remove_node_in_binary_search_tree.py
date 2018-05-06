"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
"""
若要删除一个BST的一个结点，需要考虑如下三种情况：

需要删除的节点下并没有其他子节点
需要删除的节点下有一个子节点（左或右）
需要删除的节点下有两个子节点（既左右节点都存在）
对这三种情况分别采取的措施是：

直接删除此结点
删除此结点，将此结点父节点连接到此结点左（右）子树
找出此结点右子树中的最小结点，用以代替要删除的结点，然后删除此最小结点
"""

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        if root is None:
            return None
        if root.val > value:
            root.left = self.removeNode(root.left, value)
        elif root.val < value:
            root.right = self.removeNode(root.right, value)
        else:
            if root.left is None or root.right is None:
                root = root.left if root.left is not None else root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.removeNode(root.right, cur.val)
        return root
