class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        if s is None or len(s) == 0:
            return s
        s_list = s.split()
        s_list.reverse()
        return ' '.join(s_list)