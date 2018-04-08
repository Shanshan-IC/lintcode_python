class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """

    def helpPow(self, x, n):
        if x == 1 or n == 0:
            return 1
        tmp = self.helpPow(x, n / 2)
        if n & 1:
            return tmp * tmp * x
        else:
            return tmp * tmp

    def myPow(self, x, n):
        if x == 0:
            return 0
        if n < 0:
            return 1 / self.helpPow(x, -n)
        else:
            return self.helpPow(x, n)