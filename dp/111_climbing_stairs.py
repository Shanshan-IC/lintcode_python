'''
dp[i]表示i个台阶需要的次数
dp[i] = dp[i-1] + dp[i-2]
'''


class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if n == 0:
            return 0
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n - 1]

# 或者
class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if n == 0:
            return 0
        first, second = 1, 2
        for i in range(2, n):
            next = first + second
            first = second
            second = next
        return second if n > 1 else first