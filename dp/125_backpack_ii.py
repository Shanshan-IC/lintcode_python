'''
和1的问题类似
dp[j]表示对于空间j可以获得的最大价值
dp[j] = max(dp[j], dp[j-A[i]]+V[i])
'''


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        dp = [0 for _ in range(m + 1)]
        for i in range(len(A)):
            for j in range(m, 0, -1):
                if j >= A[i]:
                    dp[j] = max(dp[j], dp[j - A[i]] + V[i])
        return dp[m]
