class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        if n== 0:
            return 0
        neg = 1
        if n < 0:
            neg, n = -1, -n
        reverse = 0
        while n:
            reverse = reverse * 10 + n % 10
            n /= 10
        reverse *= neg
        if reverse > (1<<32-1) or reverse < -(1 << 31):
            return 0
        return reverse