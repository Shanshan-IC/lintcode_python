"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class SegmentTree(object):
    def __init__(self, start, end, sum=0):
        self.start = start
        self.end = end
        self.sum = sum
        self.left, self.right = None, None

    @classmethod
    def build(cls, start, end, a):
        if start > end:
            return None
        root = SegmentTree(start, end, a[start])
        if start == end:
            return root
        root.left = cls.build(start, (start + end) / 2, a)
        root.right = cls.build((start + end) / 2 + 1, end, a)
        root.sum = root.left.sum + root.right.sum
        return root

    @classmethod
    def query(self, root, start, end):
        if root.start > end or root.end < start:
            return 0
        if start <= root.start and root.end <= end:
            return root.sum
        return self.query(root.left, start, end) + self.query(root.right, start, end)


class Solution:
    """
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """
    def intervalSum(self, A, queries):
        root = SegmentTree.build(0, len(A)-1, A)
        res = []
        for q in queries:
            res.append(SegmentTree.query(root, q.start, q.end))
        return res
