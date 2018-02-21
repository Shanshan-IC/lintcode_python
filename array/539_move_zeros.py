class Solution:
    """
    @param: nums: an integer array
    @return:
    """
    def moveZeroes(self, nums):
        if nums is None or len(nums) == 0:
            return nums
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
