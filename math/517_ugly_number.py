class Solution:
    """
    @param: num: An integer
    @return: true if num is an ugly number or false
    """
    def isUgly(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        while n >= 2 and n % 2 == 0:
            n /= 2
        while n >= 3 and n % 3 == 0:
            n /= 3
        while n >= 5 and n % 5 == 0:
            n /= 5
        return n == 1