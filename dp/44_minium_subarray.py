class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        l = len(nums)
        if l <= 0:
            return 0
        mins, cur = 2**31-1, 0
        for num in nums:
            if cur > 0:
                cur = num
            else:
                cur += num
            if cur < mins:
                mins = cur
        return mins