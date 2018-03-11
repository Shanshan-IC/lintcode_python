class Solution:
    """
    @param A: An integer array
    @param index1: the first index
    @param index2: the second index
    @return: nothing
    """
    def swapIntegers(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]
