class Solution:
    """
    @param: n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        dict = {}
        dict[n] = 1
        while n != 1:
            n = sum([int(x) * int(x) for x in list(str(n))])
            if n in dict:
                return False
            dict[n] = 1
        return True