class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        le = len(nums)
        l = [ 1 for i in xrange(le + 1)]
        for i in xrange(le - 1, 0, -1):
            l[i] = l[i+1] * nums[i]
        r = 1
        res = []
        for i in xrange(le):
            res.append(l[i+1] * r)
            r *= nums[i]
        return res