'''
与最长公共子序列相似，利用动态规划，动态转移方程为：

如果xi == yj， 则 c[i][j] = c[i-1][j-1]+1
如果xi ! = yj, 那么c[i][j] = 0
'''
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        m, n, res = len(A), len(B), 0
        if m == 0 or n == 0:
            return 0
        dp = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
        return res            