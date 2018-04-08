'''
从后往前找，找到第一对(i,j)，使得 nums[i] < num[j] ,然后将两者交换后，后面部分排序即可。
'''

class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        if len(nums) == 0:
            return []
        for i in xrange(len(nums)-1, -1, -1):
            for j in xrange(len(nums)-1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    tmp = sorted(nums[i+1:])
                    for n in tmp:
                        nums[i+1] = n
                        i += 1
                    return
        nums.sort()
        return