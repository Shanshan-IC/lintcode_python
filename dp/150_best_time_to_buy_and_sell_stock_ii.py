import sys
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        res = 0
        low, high = sys.maxint, sys.maxint
        for p in prices:
            if p > high:
                high = p
            else:
                res += (high - low)
                high, low = p, p
        return res + (high - low)