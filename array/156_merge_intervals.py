class Solution:
    """
    @param: intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        intervals.sort()
        res = []
        start, end, l = 0, 1, len(intervals)
        if l < 2:
            return intervals
        while end < l:
            while end < l and start < l and intervals[end][0] <= intervals[start][-1]:
                end += 1
            res.append([intervals[start][0], intervals[end - 1][-1]])
            start = end
            end += 1
        if end == start:
            res.append(intervals[-1])
        print(res)
        return res

Solution().merge([[1,4],[1,4]])