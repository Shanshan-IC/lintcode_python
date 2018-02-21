class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        a ^= b
        cnt = 0
        for i in range(0, 32):
            if a & 1:
                cnt += 1
            a >>= 1
        return cnt
