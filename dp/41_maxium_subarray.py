class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        l = len(nums)
        if l <= 0:
            return 0
        maxs, cur = -2**31, 0
        for num in nums:
            if cur < 0:
                cur = num
            else:
                cur += num
            if cur > maxs:
                maxs = cur
        return maxs