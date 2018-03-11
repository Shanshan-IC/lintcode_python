'''
当i为奇数时，nums[i] >= nums[i - 1]
当i为偶数时，nums[i] <= nums[i - 1]
那么只要对每个数字，根据其奇偶性，选择是否与上一个数交换即可
'''

class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        l = len(nums)
        for i in xrange(1, l):
            if i % 2 == 1 and nums[i] < nums[i - 1] or \
                i % 2 == 0 and nums[i] > nums[i - 1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]