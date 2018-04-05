'''
因为数的范围是1~100，每个数有100中调整的可能性，采用动态规划的思路。
建立大小为(n+1)*101的二维数组rec记录所有可能调整的代价，第一行初始化为全0，其他行为最大值。
dp中第i行对应A[i-1]。对于每个数A[i]，调整后的结果有100种，用dp[i][j]表示数字A[i]调整为j的最小代价。
对于每个dp[i][j]，A[i-1]调整到k的代价加上A[i]调整到j的最小代价即为dp[i][j]的代价。而k又有100种选择，对于j，当|j-k|的绝对值不大于target时，代价最小，
当前dp[i][j]为dp[i-1][k] +( j - A[i-1])，dp[i][j]保留所有可能代价中的最小代价。
最后，dp[n][0~100]中的最小代价即为对整个数组调整后的最下代价。
'''
class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        dp = [[sys.maxint for _ in xrange(101)] for _ in xrange(len(A)+1)]
        for i in xrange(101):
            dp[0][i] = 0
        for i in xrange(1, len(A)+1):
            for j in xrange(101):
                if dp[i-1][j] != sys.maxint:
                    for k in xrange(101):
                        if abs(j-k) <= target:
                            dp[i][k] = min(dp[i][k], dp[i-1][j]+abs(k-A[i-1]))
        res = sys.maxint
        for i in xrange(101):
            res = min(res, dp[len(A)][i])
        return res