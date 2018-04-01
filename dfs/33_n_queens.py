class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    n = 0
    res = []
    cols = {}

    def isAttack(self, row, col):
        for c, r in self.cols.iteritems():
            if r - c == row - col or r + c == row + col:
                return True
        return False

    def solveNQueens(self, n):
        self.n = n
        self.dfs(0)
        return self.res

    def dfs(self, row):
        if row == self.n:
            res = []
            for i in xrange(self.n):
                r = ['.'] * self.n
                r[self.cols[i]] = 'Q'
                res.append(''.join(r))
            self.res.append(res)
            return
        for col in xrange(self.n):
            if col in self.cols:
                continue
            if self.isAttack(row, col):
                continue
            self.cols[col] = row
            self.dfs(row + 1)
            del self.cols[col]