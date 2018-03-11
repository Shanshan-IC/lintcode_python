'''
使用动态规划，用一维数组 dp[i] 表示 正整数 i 的完美平方数。正整数 i 的完美平方数 = min(和为 i 的 2 个数的完美平方数之和)
动态转移方程为 dp[i] = min(dp[i], dp[i-j] + dp[j])
'''
import sys
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        if n <= 1:
            return 1
        dp = [sys.maxint for _ in xrange(n+1)]
        dp[1] = 1
        for i in xrange(1, n+1):
            mid = int(math.sqrt(i))
            if mid * mid == i:
                dp[i] = 1
            else:
                for j in xrange(1, i/2+1):
                    dp[i] = min(dp[i], dp[i-j]+dp[j])
        return dp[n]
