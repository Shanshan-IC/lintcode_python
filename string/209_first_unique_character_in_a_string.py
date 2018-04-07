class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        d = {}
        for s in str:
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        for s in str:
            if d[s] == 1:
                return s
        return ""