'''
使用前后遍历，分别求出 0-i 的最大值和 i+1-size-1 的最大值。
left[i] 表示0 - i 这段数组的最大收益
right[i] 表示i - A.length-1 这段数组的最大收益
'''
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if prices is None or len(prices) < 2:
            return 0
        n = len(prices)
        left = [0] * n
        right = [0] * n
        minV = prices[0]
        for i in range(1, n):
            minV = min(minV, prices[i])
            left[i] = max(left[i-1], prices[i] - minV)
        maxV = prices[n-1]
        for i in range(n-2, -1, -1):
            maxV = max(maxV, prices[i])
            right[i] = max(right[i+1], maxV - prices[i])
        res = 0 
        for i in range(0, n):
            res = max(res, left[i] + right[i])
        return res        
