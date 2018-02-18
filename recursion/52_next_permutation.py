class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """

    def nextPermutation(self, nums):
        if len(nums) <= 0:
            return nums
        # 从后往前找，找到第一对(i,j)，使得 nums[i] < num[j] ,然后将两者交换后，后面部分排序即可。
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    if i + 1 < len(nums) - 1:
                        nums = nums[:i+1] + sorted(nums[i+1:])
                    return nums
        nums.sort()
        return nums