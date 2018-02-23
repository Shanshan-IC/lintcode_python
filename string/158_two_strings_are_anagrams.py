class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        if len(s) != len(t):
            return False
        d = {}
        for a in s:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        for a in t:
            if a not in d or d[a] < 1:
                return False
            d[a] -= 1
        return True
