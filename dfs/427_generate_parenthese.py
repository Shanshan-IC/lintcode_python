class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """

    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helper('', res, n, n)
        return res

    def helper(self, tmp, res, l, r):
        if l > r:
            return
        if l == 0 and r == 0:
            return res.append(tmp)
        if l > 0:
            self.helper(tmp + '(', res, l - 1, r)
        if r > 0:
            self.helper(tmp + ')', res, l, r - 1)

