class Solution:
    """
    @param: : A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        nums.sort()
        return nums[(len(nums)-1)/2]