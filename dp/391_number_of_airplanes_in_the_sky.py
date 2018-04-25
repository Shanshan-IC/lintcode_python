"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
使用 map 记录起飞时刻与降落时刻飞机的数量，起飞时刻飞机数量 +1，降落时刻飞机数量 -1，然后将时刻排序，遍历排序后的时刻，寻找出最大值
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        times_point = []
        for air in airplanes:
            times_point.append((air.start, 1))
            times_point.append((air.end, -1))
        times_point.sort(cmp=self.cmp)
        s, maxs = 0, 0
        for t, delta in times_point:
            s += delta
            maxs = max(maxs, s)
        return maxs

    def cmp(self, a, b):
        if a[0] != b[0]:
            return a[0] - b[0]
        return a[1] - b[1]