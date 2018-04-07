class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            while l < r and nums[l]&1:
                l += 1
            while l < r and nums[r]&1 == 0:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
