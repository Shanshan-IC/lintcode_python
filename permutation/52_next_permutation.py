# -*- coding:utf-8 -*-

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """

    def nextPermutation(self, nums):
        if nums is None or len(nums) <= 0:
            return nums
        # 例如，[1,3,5,4,2]
        # 从后往前找，找到第一个nums[i] > nums[i-1]，找到3
        l = len(nums)
        i = l - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        i -= 1
        if i == -1:
            nums.reverse()
            return nums
        # 从找到的i出发，找到后面比3大的最小值，交换二者，找到4
        j = i + 1
        for idx in range(i + 1, l):
            if nums[idx] > nums[i] and nums[idx] <= nums[j]:
                j = idx
        print(i, j)
        nums[i], nums[j] = nums[j], nums[i]
        # 对i 后面的进行排序，对[5,3,2]进行排序
        back = sorted(nums[i + 1:])
        nums[i + 1:] = back
        return nums

