class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = left + (right-left) / 2
            if nums[mid] == target:
                if (mid - 1 >= 0 and nums[mid-1] == target):
                    right = mid
                else:
                    return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return res