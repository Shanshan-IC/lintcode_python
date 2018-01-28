class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        cnt = 0
        for x in xrange(32):
            cnt += num & 1
            num >>= 1
        return cnt