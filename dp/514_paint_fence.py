'''

使用动态规划，用一维数组 dp[i] 记录前 i 个柱子的染色方案。染色时需要注意的是最多允许 2 颗相邻的柱子具有相同的颜色。

第 1 颗柱子染色方案为色彩总数 k，因为没有相邻的柱子
第 2 颗柱子染色方案为色彩总数 k * k，因为只有 2 颗柱子，相邻柱子颜色可以相同
第 3 颗及其之后的柱子，染色方案为色彩总数 dp[i-2] * (k-1) + dp[i-1] * (k-1)，因为若此柱子要染得颜色与上一颗柱子相同，则一定不能与上上颗相同；若与上一颗不同，则无需考虑其他柱子
'''

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        if n <= 0:
            return 0
        dp = [0 for _ in xrange(n)]
        dp[0] = k
        if n == 1:
            return k
        dp[1] = k * k
        for i in xrange(2, n):
            dp[i] = dp[i-2]*(k-1) + dp[i-1]*(k-1)
        return dp[n-1]

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        if n <= 0:
            return 0
        if n == 1:
            return k
        first, second = k, k * k
        for i in xrange(2, n):
            tmp = first
            first = second
            second = (tmp + second) * (k-1)
        return second