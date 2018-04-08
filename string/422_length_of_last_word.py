class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        res = s.split()
        return len(res[-1]) if len(res) > 0 else 0