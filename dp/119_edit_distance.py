'''
使用动态规划，用二维数组dp[i][j]表示第一个字符串到i第二个字符串到j的时候需要进行多少次修改
动态转移方程为：
dp[i][j] = dp[i-1][j-1] + dp[i-1][j] （S[i]==T[j]）
dp[i][j] = dp[i-1][j] （S[i]!=T[j]）
'''
class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[m][n]