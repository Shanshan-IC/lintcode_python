class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False for _ in xrange(n+1)] for _ in xrange(m+1)]
        dp[0][0] = True
        if m == 0 and p.count('*') == n:
            return True
        for i in xrange(m+1):
            for j in xrange(n+1):
                if i > 0 and j > 0:
                    dp[i][j] |= dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] in ['?', '*'])
                    dp[i][j] |= dp[i-1][j] and p[j-1] == '*'
                if j > 0:
                    dp[i][j] |= dp[i][j-1] and p[j-1] == '*'
        return dp[m][n]