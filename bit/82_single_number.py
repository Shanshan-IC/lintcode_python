class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        res = 0
        for a in A:
            res ^= a
        return res