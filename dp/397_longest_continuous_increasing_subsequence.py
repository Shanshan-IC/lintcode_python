class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        if A is None or len(A) == 0:
            return 0
        mx, cur = 1, 1
        for i in xrange(1, len(A)):
            if A[i] > A[i-1]:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 1
        cur = 1
        for i in xrange(1, len(A)):
            if A[i] < A[i-1]:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 1
        return mx