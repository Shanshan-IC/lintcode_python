class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid is None or len(obstacleGrid) == 0:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 0 or n == 0:
            return 0
        dp = [[0] * n] * m
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

