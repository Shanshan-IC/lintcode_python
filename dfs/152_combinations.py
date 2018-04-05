class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    res = []

    def combine(self, n, k):
        self.dfs(n, k, 1, 0, [])
        return self.res

    def dfs(self, n, k, i, j, tmp):
        if j == k:
            self.res.append(tmp[:])
            return
        for i in xrange(i, n + 1):
            tmp.append(i)
            self.dfs(n, k, i + 1, j + 1, tmp)
            tmp.pop()