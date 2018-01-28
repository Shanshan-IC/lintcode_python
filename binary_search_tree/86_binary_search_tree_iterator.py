"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.st = []
        self.cur = root

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return self.cur or len(self.st) > 0

    """
    @return: return next node
    """
    def next(self):
        while self.cur:
            self.st.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.st.pop()
        nxt = self.cur
        self.cur = self.cur.right
        return nxt