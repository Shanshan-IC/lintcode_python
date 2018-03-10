'''
dp[i] 记录s[i]...s[n-1]的最小切割数，状态转移方程为：dp[i] = min{dp[j]+1, dp[i]} (j=i+1...n-1)
将回文结果保存至二维数组 isPalindrome[i][j] 中，若 isPalindrome[i][j] = true，则 s[i]...s[j] 是回文串
'''


class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def minCut(self, s):
        if s is None or len(s) == 0:
            return 0
        ll = len(s)
        dp = [ll - i - 1 for i in range(ll + 1)]
        record = [[False for _ in range(ll)] for _ in range(ll)]
        for i in range(ll - 1, -1, -1):
            for j in range(i, ll):
                if s[j] == s[i] and (j - i < 2 or record[i + 1][j - 1]):
                    record[i][j] = True
                    dp[i] = min(dp[i], dp[j + 1] + 1)
        return dp[0]


