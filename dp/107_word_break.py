'''
dp[i] 表示s的前i个字符可否被字典中的词分词成功

'''
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0
        n = len(s)
        f = [False] * (n+1)
        f[0] = True
        maxL = max([len(w) for w in dict])
        for i in range(1, n + 1):
            for j in range(1, min(i, maxL)+1):
                if not f[i-j]:
                    continue
                if s[i-j: i] in dict:
                    f[i] = True
                    break
        return f[n]