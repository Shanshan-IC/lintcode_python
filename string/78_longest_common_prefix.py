class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""
        end, l = 0, min([len(s) for s in strs])
        while end < l:
            for i in xrange(1, len(strs)):
                if strs[i][end] != strs[i-1][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end]
