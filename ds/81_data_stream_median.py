'''
使用一个最大堆 maxSet 与最小堆 minSet（ maxSet 用 multiset 的反向遍历代替）。maxSet 存的是到目前为止较小的那一半数，minSet 存的是到目前为止较大的那一半数，这样中位数只有可能是 maxSet 的堆顶元素（本题中）或者是两个堆顶元素的均值。
minSet与maxSet交替使用，保证两个堆的大小之差不超过1。
当插入一个新数时，若新数大于 minSet 的堆顶元素，说明新数在所有数的下半部分，此时将新数插入 minSet，取出 minSet 堆顶元素并插入至 maxSet ；否则，说明新数在所有数的上半部分，将新数插入 maxSet
当插入一个新数时，若新数小于 maxSet 的堆顶元素，说明新数在所有数的上半部分，此时将新数插入 maxSet，取出 maxSet 堆顶元素并插入至 minSet ；否则，说明新数在所有数的下半部分，将新数插入 minSet
将 maxSet 堆顶元素存入返回值数组，但不取出堆顶元素
'''
import heapq


class Solution:
    minH, maxH = [], []
    number = 0
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        res = []
        for num in nums:
            self.add(num)
            res.append(self.getM())
        return res

    def getM(self):
        return -self.maxH[0]

    def add(self, num):
        if self.number & 1:
            heapq.heappush(self.minH, num)
        else:
            heapq.heappush(self.maxH, -num)
        self.number += 1
        if len(self.maxH) == 0 or len(self.minH) == 0:
            return
        if -self.maxH[0] > self.minH[0]:
            maxs = -self.maxH[0]
            mins = self.minH[0]
            heapq.heapreplace(self.maxH, -mins)
            heapq.heapreplace(self.minH, maxs)