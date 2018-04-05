'''
left 指向第一个非0的数，right 指向倒数第一个非 2 的数，i 指向0时与 nums[l] 交换，指向 2 时与 nums[r] 交换，指向 1 则继续向后指。
'''

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        left, right = 0, len(nums)-1
        for i in xrange(len(nums)):
            while left == i and nums[left] == 0:
                left += 1
                i += 1
            while left <= right and nums[right] == 2:
                right -= 1
            if i <= right:
                if nums[i] == 0:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
                elif nums[i] == 2:
                    nums[right], nums[i] = nums[i], nums[right]
                    right -= 1
                else:
                    i += 1