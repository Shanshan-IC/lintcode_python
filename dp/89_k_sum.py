class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        if A is None or len(A) == 0 or k > len(A) or k <= 0:
            return 0
        dp = [[0 for _ in xrange(target+1)] for _ in xrange(k+1)]
        dp[0][0] = 1
        for i in xrange(len(A)):
            for j in xrange(k, 0, -1):
                for s in xrange(target, A[i]-1, -1):
                    dp[j][s] += dp[j-1][s-A[i]]
        return dp[k][target]