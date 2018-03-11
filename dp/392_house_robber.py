'''
使用动态规划，用一维数组 dp[i] 存储打劫第 i 所房屋时，最大收入。
dp[i] 的值仅仅和 dp[i -1]和 dp[i - 2] 有关，动态转移方程为
dp[i] = max(dp[i - 1], dp[i - 2] + A[i])
'''
class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if A is None or len(A) == 0:
            return 0
        l = len(A)
        dp = [0 for _ in xrange(l)]
        dp[0] = A[0]
        if l == 1:
            return A[0]
        dp[1] = max(A[0], A[1])
        for i in xrange(2, l):
            dp[i] = max(dp[i-1], dp[i-2]+A[i])
        return dp[l-1]
