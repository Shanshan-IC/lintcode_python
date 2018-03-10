'''
参考博客http://blog.sina.com.cn/s/blog_5ce680a40102vqgu.html 的递推思路，使用卡特兰数，另外使用动态规划，使用一维数组 dp[i] 保存由 i 个节点组成的不同的二叉查找树的种类
卡特兰数的递推公式为：
f(n) = f(n-1)f(0) + f(n-2)f(1) + f(n-3)f(2) + ... + f(1)f(n-2) + f(n-1)f(0)
'''
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        if n == 0 or n == 1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(0, n):
                dp[i] += dp[i-j-1] * dp[j]
        return dp[n]