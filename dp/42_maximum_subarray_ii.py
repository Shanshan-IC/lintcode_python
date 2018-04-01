'''
这个题的思路是，因为 两个subarray 一定不重叠

所以必定存在一条分割线

分开这两个 subarrays

所以 最后的部分里：

  max = Integer.MIN_VALUE;

        for(int i = 0; i < size - 1; i++){

            max = Math.max(max, left[i] + right[i + 1]);

        }

        return max;

这里是在枚举 这条分割线的位置

然后 left[] 和 right[] 里分别存的是，某个位置往左的 maximum subarray 和往右的 maximum subarray
'''
class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        n = len(nums)
        a, aa, b, bb = nums[:], nums[:], nums[:], nums[:]
        for i in xrange(1, n):
            a[i] = max(nums[i], nums[i]+a[i-1])
            aa[i] = max(a[i], aa[i-1])
        for i in xrange(n-2, -1, -1):
            b[i] = max(nums[i], nums[i] + b[i+1])
            bb[i] = max(b[i], bb[i+1])
        res = -65535
        for i in xrange(n-1):
            res = max(res, aa[i] + bb[i+1])
        return res