class Solution:
    """
    @param: n: An integer
    @return: An array storing 1 to the largest number with n digits
    """
    def numbersByRecursion(self, n):
        res = []
        top = pow(10, n)
        for i in xrange(1, top):
            res.append(i)
        return res