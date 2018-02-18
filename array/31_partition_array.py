class Solution:
    """
    @param: nums: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        i, j = 0, len(nums) - 1
        while i <= j:
            while i <= j and nums[i] < k:
                i += 1
            while i <= j and nums[j] >= k:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return i