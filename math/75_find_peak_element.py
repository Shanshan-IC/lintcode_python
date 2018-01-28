class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        if not A:
            return -1
        l, r = 0, len(A) - 1
        while l + 1 < r:
            m = l + (r-l) / 2
            if A[m] < A[m-1]:
                r = m
            elif A[m] < A[m+1]:
                l = m
            else:
                return m
        m = l if A[l] > A[r] else r
        return m