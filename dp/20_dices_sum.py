'''
用二维数组 dp[i][j] 表示 i 颗骰子所能掷出点数为 j 的次数
初始状态，1个骰子，dp[1][j] = 1 (1<=j<=6)
再加上1个骰子，此时 2 颗骰子所能掷出的点数为 2-12，
此时投掷的结果与上一次投掷的结果相关，若 2 颗骰子投出 j 点，则要求第 1 颗投掷投出 k 点且第 2 颗投出 j - k 点（j > k） ，例如 dp[2][2] = dp[1][1]，dp[2][3] = dp[1][1] + dp[1][2]
一般化，加至第 i 颗骰子后，此时 i 颗骰子所能掷出的点数为 i 到 6 * i，此时投掷的结果与前 i - 1次投掷的结果相关，若 i 颗骰子投出 j 点，则要求前 i - 1 颗投掷投出 k 点且第 2 颗投出 j - k点（j > k） ，即 dp[i][j] = dp[i-1][j-1] + dp[i-1][j-2] + dp[i-1][j-3] + dp[i-1][j-4] + dp[i-1][j-5] + dp[i-1][j-6]
'''
class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        dp = [[0 for _ in range(6*n+1)] for _ in range(n+1)]
        for i in range(1, 7):
            dp[1][i] = 1
        for i in range(2, n+1):
            for j in range(i, 6*i+1):
                for k in range(1, 7):
                    if j - k > 0:
                        dp[i][j] += dp[i-1][j-k]
        res = []
        sum = 0.0
        for i in range(n, 6*n+1):
            sum += dp[n][i]
        for i in range(n, 6*n+1):    
            res.append([i, dp[n][i] / sum])
        return res