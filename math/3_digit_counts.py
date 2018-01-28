class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        cnt = 0
        for a in xrange(n+1):
            cnt += str(a).count(str(k))
        return cnt