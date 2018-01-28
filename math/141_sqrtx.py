class Solution:
    """
    @param: x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x < 0:
            return -1
        if x == 0:
            return 0
        l, r = 1, x
        while l + 1 < r:
            m = l + (r-l)/2
            val = m**2
            if val == x:
                return m
            elif val < x:
                l = m
            else:
                r = m
        return l