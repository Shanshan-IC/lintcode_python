'''
dp[i][j] 表示A[i]和B[j]的最长公共子序列
如果A[i] == B[j], dp[i][j] = dp[i-1][j-1]+1
如果A[i] != B[j], dp[i][j] = max(dp[i-1][j], dp[i][j-1])
'''
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[m][n]