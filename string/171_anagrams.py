class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        d = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in d:
                d[tmp] = [s]
            else:
                d[tmp].append(s)
        res = []
        for item in d:
            if len(d[item]) > 1:
                res += d[item]
        return res

