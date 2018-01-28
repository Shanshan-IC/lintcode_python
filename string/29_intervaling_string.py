class Solution:
    """
    @param: s1: A string
    @param: s2: A string
    @param: s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if s3[0] != s1[0] and s3[0] != s2[0]:
            return False
        if s3[0] == s1[0] and s3[0] == s2[0]:
            return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
        if s3[0] == s1[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        return self.isInterleave(s1, s2[1:], s3[1:])