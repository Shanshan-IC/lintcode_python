class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        l = m + n
        if l & 1:
            return self.findK(A, B, l / 2 + 1)
        else:
            return (self.findK(A, B, l / 2) + self.findK(A, B, l / 2 + 1)) / 2.0

    def findK(self, A, B, l):
        if len(A) == 0:
            return B[l - 1]
        if len(B) == 0:
            return A[l - 1]
        if l == 1:
            return min(A[0], B[0])
        a = A[l / 2 - 1] if len(A) >= l / 2 else None
        b = B[l / 2 - 1] if len(B) >= l / 2 else None
        if b is None or (a is not None and a < b):
            return self.findK(A[l / 2:], B, l - l / 2)
        return self.findK(A, B[l / 2:], l - l / 2)
