'''
一次遍历 + 二分查找，首先遍历数组 A，之后以 A[i] 为目标，对数组 B 进行二分查找，找出 B 中与 A[i] 的最小差
先给两个列表排序
'''
class Solution:
    """
    @param A: An integer array
    @param B: An integer array
    @return: Their smallest difference.
    """
    def smallestDifference(self, A, B):
        A.sort()
        B.sort()
        res = sys.maxint
        for a in A:
            l, r = 0, len(B) - 1
            while l <= r:
                m = l + (r-l)/2
                if B[m] == a:
                    return 0
                elif B[m] > a:
                    r = m - 1
                else:
                    l = m + 1
            res = min(res, abs(a - B[m]))
            if m > 0:
                res = min(res, abs(a - B[m-1]))
            if m < len(B) - 1:
                res = min(res, abs(a - B[m+1]))
        return res
