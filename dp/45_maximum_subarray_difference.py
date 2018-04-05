'''
复用“求最大字数组和”的代码,求出从左自右遍历数的最大子数组maxLeft、最小子数组minLeft和从右自左遍历数的最大子数组maxRight、最小子数组minRight。然后求出maxLeft与minRight的最大差，minLeft与maxRight的最大差。即可得出最大子数组差。

'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        n = len(nums)
        a, aa, b, bb, c, cc, d, dd = nums[:], nums[:], nums[:], nums[:], nums[:], nums[:], nums[:], nums[:]
        for i in xrange(1, n):
            a[i] = max(nums[i], nums[i]+a[i-1])
            aa[i] = max(a[i], aa[i-1])
            c[i] = min(nums[i], nums[i]+c[i-1])
            cc[i] = min(c[i], cc[i-1])
        for i in xrange(n-2, -1, -1):
            b[i] = max(nums[i], nums[i] + b[i+1])
            bb[i] = max(b[i], bb[i+1])
            d[i] = min(nums[i], nums[i] + d[i+1])
            dd[i] = min(d[i], dd[i+1])
        res = -1
        for i in xrange(n-1):
            res = max([res, abs(aa[i] - dd[i+1]), abs(cc[i] - bb[i+1])])
        return res
