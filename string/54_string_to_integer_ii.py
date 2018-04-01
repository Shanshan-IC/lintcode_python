class Solution:
    """
    @param str: A string
    @return: An integer
    """

    def atoi(self, str):
        str = str.strip()
        if str == '':
            return 0
        i, res, sign = 0, 0, 1
        MaxInt = (1 << 31) - 1
        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            i += 1
        for i in xrange(i, len(str)):
            if str[i] < '0' or str[i] > '9':
                break
            res = res * 10 + int(str[i])
            if res > MaxInt:
                break
        res *= sign
        if res > MaxInt:
            return MaxInt
        if res < MaxInt * -1:
            return MaxInt * -1 - 1
        return res
