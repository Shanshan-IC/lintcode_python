"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The count number in the interval [start, end]
    """
    def query(self, root, start, end):
        if root is None or start > root.end or end < root.start:
            return 0
        if start <= root.start and end >= root.end:
            return root.count
        return self.query(root.left, start, end) + self.query(root.right, start, end)