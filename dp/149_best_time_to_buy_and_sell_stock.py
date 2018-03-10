class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        res = 0
        low, high = sys.maxint, 0
        for p in prices:
            if p - low > res:
                res = p - low
            low = min(p, low)
        return res