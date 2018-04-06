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
        
    @classmethod    
    def modify(self, root, index, value):
        if root is None:
            return 0
        if root.start == root.end:
            root.sum = value
            return
        if root.left.end >= index:
            self.modify(root.left, index, value)
        else:
            self.modify(root.right, index, value)
        root.sum = root.left.sum + root.right.sum

class Solution:
    """
    @param: A: An integer array
    """
    def __init__(self, A):
        self.root = SegmentTree.build(0, len(A)-1, A)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        return SegmentTree.query(self.root, start, end)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        SegmentTree.modify(self.root, index, value)