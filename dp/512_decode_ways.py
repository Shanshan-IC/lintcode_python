'''
使用动态规划，用一维数组 dp[i] 表示加密消息中前 i 位有多少种解法。因为有效的解在 1 - 26 之间，所以要注意有效解（可能会出现无解的消息，如 100 ）特别是 0 的出现。
'''

class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        if s is None or len(s) == 0 or s[0] == '0':
            return 0
        dp = [0 for _ in xrange(len(s)+1)]
        dp[0] = 1
        dp[1] = 1
        for i in xrange(2, len(s)+1):
            if 10 <= int(s[i - 2 : i]) <= 26 and s[i - 1] != '0':
                dp[i] = dp[i - 1] + dp[i - 2]
            elif int(s[i-2 : i]) == 10 or int(s[i - 2 : i]) == 20:
                dp[i] = dp[i - 2]
            elif s[i-1] != '0':
                dp[i] = dp[i-1]
            else:
                return 0
        return dp[len(s)]