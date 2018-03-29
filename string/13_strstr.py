class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        s, t = len(source), len(target)
        if s < t:
            return -1
        for i in xrange(s-t+1):
            j = 0
            while (j < t):
                if source[i+j] != target[j]:
                    break
                j += 1
            if j == t:
                return i
        return -1