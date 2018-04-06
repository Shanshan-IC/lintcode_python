'''
首先对候选数字排序、剔重，然后采取回溯和递归

'''


class Solution:
    res = []
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        candidates = list(set(candidates))
        candidates.sort()
        l = len(candidates)
        self.dfs(candidates, target, 0, [], l)
        return self.res

    def dfs(self, candidates, target, pos, tmp, l):
        if target == 0:
            self.res.append(tmp)
            return
        for i in xrange(pos, l):
            if target < candidates[i]:
                return
            self.dfs(candidates, target - candidates[i], i, tmp + [candidates[i]], l)