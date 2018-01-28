"""
先根据f(1)和f(2)计算出f(3)，再根据f(2)和f(3)计算出f(4)……依次类推，最后计算出f(n)。可以看到迭代方法的时间复杂度只有O(n)。
"""

class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        if n <= 2:
            return n - 1
        first = 0
        second = 1
        for i in range(3, n+1):
            second = first + second
            first = second - first
        return second