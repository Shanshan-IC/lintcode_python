'''
对于i个物品在j空间下能装满的大小dp[i][j]：
不放第i个物品
dp[i][j] = dp[i-1][j]
放第i个物品
dp[i][j] = dp[i-1][j-A[i]]+A[i]
所以转移方程是dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i]]+A[i])
'''
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        if A is None or len(A) == 0 or m < 0:
            return 0
        dp = [0 for _ in range(m+1)]
        for i in range(len(A)):
            for j in range(m, 0, -1):
                if j >= A[i]:
                    dp[j] = max(dp[j], dp[j-A[i]] + A[i])
        return dp[m]