class Solution:
    res = []
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        candidates.sort()
        l = len(candidates)
        used = [0] * len(candidates)
        self.dfs(candidates, target, 0, 0, [], used)
        return self.res

    def dfs(self, candidates, target, pos, now, tmp, used):
        if now == target:
            self.res.append(tmp[:])
            return
        for i in xrange(pos, len(candidates)):
            if now+candidates[i] <= target and (i == 0 or candidates[i] != candidates[i-1] or used[i-1] == 1):
                tmp.append(candidates[i])
                used[i] = 1
                self.dfs(candidates, target, i+1, now+candidates[i], tmp, used)
                used[i] = 0
                tmp.pop()
