class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        start, res = 0, 0
        last = {}
        for i in xrange(len(s)):
            if s[i] in last and last[s[i]] >= start:
                start = last[s[i]] + 1
            last[s[i]] = i
            res = max(res, i - start+1)
        return res