class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1
        l, r = 0, len(nums) - 1
        while l < r - 1:
            m = l + (r - l) / 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m
        return -1